import hashlib
import invoke
import jinja2
import re
import os
import sys
import yaml
import markdown
from datetime import datetime
import pytz
from icalendar import Calendar, Event


VERBOSE = False


def check_result(result, description):
    if result.failed:
        print('========================================')
        print('Failed to {}'.format(description))
        print('')
        print('========================================')
        print('STDOUT:')
        print('========================================')
        print(result.stdout)
        print('========================================')
        print('STDERR:')
        print('========================================')
        print(result.stderr)
        print('========================================')
        raise Exception('Failed to {}'.format(description))


@invoke.task
def verbose():
    global VERBOSE

    VERBOSE = True


@invoke.task
def update_dependencies():
    # Parameters to keep everything silent
    params_silent = {
        'encoding': sys.stdout.encoding,
        'hide': 'both' if VERBOSE is False else None,
        'warn': True
    }

    # Parse our compile config
    with open('_compile-config.yml') as f:
        compile_config_yaml = yaml.safe_load(f)

    # The npm install command sometimes outputs characters that cause Unicode
    # errors on Windows, so we set the encoding parameter on our commands
    print('Checking Node.js dependencies')
    result = invoke.run('npm install', **params_silent)
    check_result(result, 'install Node.js dependencies')

    # Python dependencies
    print('Checking Python dependencies')

    # Ensure we have a current version of pip, as needed by pip-tools
    pip_version_desired = compile_config_yaml['config']['local']['python']['pip_version']
    result = invoke.run('pip --disable-pip-version-check show pip', **params_silent)
    check_result(result, 'check pip version')

    pip_version_current = re.search('^Version: ([\d\.]+)', result.stdout, re.MULTILINE).group(1)
    if pip_version_current != pip_version_desired:
        result = invoke.run(
            'python -m pip install --upgrade pip=={}'.format(
                pip_version_desired
            ),
            **params_silent
        )
        check_result(result, 'update pip version')

    # Ensures we have pip-tools, which will be in our requirements file
    # pip-sync also does not respect options in the requirements file,
    # so installing the entire file ensures pip-sync only needs to delete
    result = invoke.run('pip --disable-pip-version-check install -r requirements3.txt', **params_silent)
    check_result(result, 'install pip requirements')
    # Ensure we have exactly our dependencies
    result = invoke.run('pip-sync requirements3.txt', **params_silent)
    check_result(result, 'sync pip requirements')

    # Ruby dependencies
    print('Checking Ruby dependencies')

    # Check we have the correct Bundler version
    bundler_version_desired = compile_config_yaml['config']['local']['ruby']['bundler_version']

    result = invoke.run('gem list -i bundler -v {}'.format(bundler_version_desired), **params_silent)
    # expected to fail if the desired version is not installed
    if result.failed:
        result = invoke.run('gem install bundler -v {}'.format(bundler_version_desired), **params_silent)
        check_result(result, 'install bundler')

    # And only the correct Bundler version
    invoke.run('gem uninstall bundler -v "!={}"'.format(bundler_version_desired), **params_silent)
    # expected to fail if no other versions of bundler are installed

    # Check we have our Ruby dependencies
    result = invoke.run('bundle check', **params_silent)
    # expected to fail if we are missing dependencies
    if result.failed:
        result = invoke.run('bundle install', **params_silent)
        check_result(result, 'bundle install')


@invoke.task(pre=[update_dependencies])
def build_production():
    invoke.run(
        'bundle exec jekyll build -t --config _config.yml,_config-production.yml',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[update_dependencies])
def build_test():
    invoke.run(
        'bundle exec jekyll build -t --config _config.yml,_config-test.yml',
        encoding=sys.stdout.encoding
    )


@invoke.task()
def compile_config():
    # Parse our compile config
    with open('_compile-config.yml') as f:
        compile_config_yaml = yaml.safe_load(f)

    # Compile each jinja2 file
    for jinja2_entry in compile_config_yaml['jinja2']['entries']:
        jinja2_environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(searchpath='.'),
            undefined=jinja2.StrictUndefined
        )
        template = jinja2_environment.get_template(jinja2_entry['in'])
        with open(jinja2_entry['out'], 'w') as f:
            f.write(template.render(compile_config_yaml['config']))


@invoke.task()
def compile_calendar():
    # Obtain our stored sequences
    with open('_compile-calendar-sequences.yml') as f:
        seminar_calendar_sequences = yaml.safe_load(f)['sequences']
    # Iterate over all our seminar files
    seminar_paths = [
        os.path.normpath(seminar_file_entry.path)
        for seminar_file_entry
        in os.scandir('_seminars')
        if seminar_file_entry.is_file() and
           os.path.normpath(seminar_file_entry.path) != os.path.normpath('_seminars/_template.md')
    ]

    regenerate_calendar_ics = True #For debugging, change to "False" before PR

    for seminar_path_current in seminar_paths:
        # Get the hash and sequence from the file, to compare against our stored data
        with open(seminar_path_current, 'rb') as f:
            seminar_hash_current = hashlib.md5(f.read()).hexdigest()
        with open(seminar_path_current) as f:
            seminar_sequence_current = list(yaml.safe_load_all(f))[0]['sequence']
        if seminar_path_current not in seminar_calendar_sequences:
            # This is a seminar that is new to our sequence tracking
            seminar_calendar_sequences[seminar_path_current] = {
                'hash': 'invalid_hash_to_force_update',
                'sequence': seminar_sequence_current
            }

        seminar_hash_stored = seminar_calendar_sequences[seminar_path_current]['hash']
        seminar_sequence_stored = seminar_calendar_sequences[seminar_path_current]['sequence']
        if seminar_hash_current != seminar_hash_stored:
            # Change detected, we need to bump the sequence
            seminar_sequence_current = max(seminar_sequence_current, seminar_sequence_stored) + 1

            # pyyaml does not preserve comments, so we brute force modification of the seminar yml file
            with open(seminar_path_current) as f:
                seminar_contents = f.read()
            seminar_contents = re.sub(
                'sequence: {}'.format(seminar_sequence_stored),
                'sequence: {}'.format(seminar_sequence_current),
                seminar_contents
            )
            with open(seminar_path_current, 'w') as f:
                f.write(seminar_contents)

            # That changed the file, so update our hash, then store the updated sequence
            with open(seminar_path_current, 'rb') as f:
                seminar_hash_current = hashlib.md5(f.read()).hexdigest()

            seminar_calendar_sequences[seminar_path_current] = {
                'hash': seminar_hash_current,
                'sequence': seminar_sequence_current
            }

            #Trigger that we need to regenerate the subscribable calendar
            regenerate_calendar_ics = True

    # Store our updated sequences
    data = {'sequences': seminar_calendar_sequences }
    with open('_compile-calendar-sequences.yml', 'w') as f:
        yaml.dump(
            data,
            stream=f,
            default_flow_style=False
        )

    if regenerate_calendar_ics:
        # Create calendar object. Unless we were to store the calendar object between runs and update it dynamically (as above), we have to re-generate the entire file every time.
        ics = Calendar()
        ics.add('prodid', '-//DUB//DUB Calendar 2.0//EN')
        ics.add('version', '2.0')
        ics.add('calscale','gregorian')
        ics.add('method', 'publish')
        ics.add('x-wr-calname', 'DUB Calendar')
        ics.add('x-wr-timezone', 'America/Los_Angeles')
        ics.add('x-wr-caldesc', 'A calendar of DUB events.')
        for seminar_path_current in seminar_paths:
            with open(seminar_path_current) as f:
                seminar_contents = list(yaml.safe_load_all(f))[0]
            # Add seminar as calendar event
            ics_event = Event()
            ics_event.add('uid', seminar_contents['date'].strftime('%Y-%m-%d') + '@dub.washington.edu')
            
            #Generate seminar string from applicable components
            summary_string = 'DUB Seminar'
            if 'no_seminar' in seminar_contents:
                #Title is reflected when there's no seminar
                summary_string = seminar_contents['title']
            else:
                #Add the location unless overridden by the page
                if 'location_override_seminar_page' in seminar_contents:
                    #Remove newlines in title
                    ics_event.add('location', re.sub('<br>', '', seminar_contents['location_override_seminar_page']))
                else:
                    ics_event.add('location', seminar_contents['location'])
                if 'tbd_speakers' not in seminar_contents:
                    speaker_names = ', '.join([' '.join(speaker['name'][1:] + [speaker['name'][0]]) for speaker in seminar_contents['speakers']])
                    #Assume the first speaker's affiliation is representative of all of them, rather than duplicating e.g., Speaker A (UW), Speaker B (UW), Speaker C (UW)
                    #This is not true in all cases. See 2016-06-22
                    first_affiliation = ''
                    if 'affiliation' in seminar_contents['speakers'][0]:
                        first_affiliation = '({})'.format(seminar_contents['speakers'][0]['affiliation'])
                    summary_string += ' - {} {}'.format(speaker_names ,first_affiliation)
                else:
                    summary_string += ' - TBD'
                if 'tbd_title' not in seminar_contents:
                    summary_string += ' - "{}"'.format(seminar_contents['title'])
                if 'title_override_seminar_page' in seminar_contents:
                    summary_string = seminar_contents['title_override_seminar_page']
            ics_event.add('summary', summary_string)
            # Generate naive time objects from seminar date and time
            seminar_start_time = datetime.combine(seminar_contents['date'], datetime.strptime(seminar_contents['time'], '%I:%M %p').time())
            seminar_end_time = datetime.combine(seminar_contents['date'], datetime.strptime(seminar_contents['time_end'], '%I:%M %p').time())
            # Localize time objects by time zone
            ics_event.add('dtstart', pytz.timezone('America/Los_Angeles').localize(seminar_start_time))
            ics_event.add('dtend', pytz.timezone('America/Los_Angeles').localize(seminar_end_time))
            #Generate description string from applicable components
            description_string = ''
            if 'text_override_seminar_page' in seminar_contents:
                description_string = seminar_contents['text_override_seminar_page']
            else:
                if 'tbd_bio' not in seminar_contents:
                    if 'tbd_abstract' not in seminar_contents:
                        description_string = seminar_contents['abstract'] + '\r\n' + seminar_contents['bio']
                    else:
                        description_string = seminar_contents['bio']
                elif 'tbd_abstract' not in seminar_contents:
                    description_string = seminar_contents['abstract']
            #parse description as markdown
            class SensibleParagraphs(markdown.extensions.Extension):
                def extendMarkdown(self, md, md_globals):
                    br_tag = markdown.inlinepatterns.SubstituteTagPattern(r'\n', None)
                    md.inlinePatterns.add('nl', br_tag, '_end')
            ics_event.add('description', markdown.markdown(description_string, extensions=[SensibleParagraphs()]))

            ics.add_component(ics_event)
        with open('calendar.ics', 'wb') as f:
            f.write(ics.to_ical())

@invoke.task()
def compile_calendar_increment_all_sequences():
    # Obtain our stored sequences
    with open('_compile-calendar-sequences.yml') as f:
        seminar_calendar_sequences = yaml.safe_load(f)['sequences']

    # Iterate over all our seminar files
    seminar_paths = [
        os.path.normpath(seminar_file_entry.path)
        for seminar_file_entry
        in os.scandir('_seminars')
        if seminar_file_entry.is_file() and
           os.path.normpath(seminar_file_entry.path) != os.path.normpath('_seminars/_template.md')
    ]

    for seminar_path_current in seminar_paths:
        # Get the hash and sequence from the file
        with open(seminar_path_current, 'rb') as f:
            seminar_hash_current = hashlib.md5(f.read()).hexdigest()
        with open(seminar_path_current) as f:
            seminar_sequence_current = list(yaml.safe_load_all(f))[0]['sequence']

        if seminar_path_current not in seminar_calendar_sequences:
            seminar_calendar_sequences[seminar_path_current] = {
                'hash': seminar_hash_current,
                'sequence': seminar_sequence_current
            }

        seminar_hash_stored = seminar_calendar_sequences[seminar_path_current]['hash']
        seminar_sequence_stored = seminar_calendar_sequences[seminar_path_current]['sequence']

        # Bump the sequence
        seminar_sequence_current = max(seminar_sequence_current, seminar_sequence_stored) + 1

        # pyyaml does not preserve comments, so we brute force modification of the seminar yml file
        with open(seminar_path_current) as f:
            seminar_contents = f.read()
        seminar_contents = re.sub(
            'sequence: {}'.format(seminar_sequence_stored),
            'sequence: {}'.format(seminar_sequence_current),
            seminar_contents
        )
        with open(seminar_path_current, 'w') as f:
            f.write(seminar_contents)

        # That changed the file, so update our hash, then store the updated sequence
        with open(seminar_path_current, 'rb') as f:
            seminar_hash_current = hashlib.md5(f.read()).hexdigest()

        seminar_calendar_sequences[seminar_path_current] = {
            'hash': seminar_hash_current,
            'sequence': seminar_sequence_current
        }

    # Store our updated sequences
    data = {'sequences': seminar_calendar_sequences }
    with open('_compile-calendar-sequences.yml', 'w') as f:
        yaml.dump(
            data,
            stream=f,
            default_flow_style=False
        )


@invoke.task()
def compile_requirements():
    # Compile the requirements file
    invoke.run(
        'pip-compile --upgrade --output-file requirements3.txt requirements3.in',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[update_dependencies])
def serve_production():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-production.yml -H 0.0.0.0',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[update_dependencies])
def serve_test():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-test.yml --watch --force_polling',
        encoding=sys.stdout.encoding
    )


@invoke.task
def update_base():
    invoke.run('git pull https://github.com/fogies/web-jekyll-base.git master', encoding=sys.stdout.encoding)
