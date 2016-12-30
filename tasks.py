import hashlib
import invoke
import jinja2
import re
import os
import posixpath
import sys
import yaml
import markdown
from datetime import datetime
import pytz
from icalendar import Calendar, Event


VERBOSE = False


@invoke.task
def verbose():
    global VERBOSE

    VERBOSE = True


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
def compile_config():
    # Parse our compile config
    with open('_compile-config.yml') as f:
        compile_config_yaml = yaml.safe_load(f)

    # Compile each jinja2 file
    for jinja2_entry in compile_config_yaml['compile_config']['entries']:
        jinja2_environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(searchpath='.'),
            undefined=jinja2.StrictUndefined
        )
        template = jinja2_environment.get_template(jinja2_entry['in'])
        with open(jinja2_entry['out'], 'w') as f:
            f.write(template.render(compile_config_yaml['config']))


@invoke.task(pre=[update_dependencies])
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

    # Maintain the sequence field for each seminar
    for seminar_path_current in seminar_paths:
        # Get the hash and sequence from the file, to compare against our stored data
        with open(seminar_path_current, 'rb') as f:
            seminar_hash_current = hashlib.md5(f.read()).hexdigest()
        with open(seminar_path_current) as f:
            seminar_sequence_current = list(yaml.safe_load_all(f))[0]['sequence']

        # Regardless of platform we're on, standardize the path we store (e.g., slashes)
        seminar_path_stored = posixpath.join(*os.path.normpath(seminar_path_current).split(os.sep))
        if seminar_path_stored not in seminar_calendar_sequences:
            # This is a seminar that is new to our sequence tracking
            seminar_calendar_sequences[seminar_path_stored] = {
                'hash': 'invalid_hash_to_force_update',
                'sequence': seminar_sequence_current
            }

        seminar_hash_stored = seminar_calendar_sequences[seminar_path_stored]['hash']
        seminar_sequence_stored = seminar_calendar_sequences[seminar_path_stored]['sequence']
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

            seminar_calendar_sequences[seminar_path_stored] = {
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

    # Now generate the ics file from our seminars and their sequences
    ics = Calendar()
    ics.add('PRODID', '-//DUB//DUB Calendar')
    ics.add('VERSION', '2.0')
    ics.add('CALSCALE','GREGORIAN')
    ics.add('METHOD', 'PUBLISH')
    ics.add('X-WR-CALNAME', 'DUB Calendar')
    ics.add('X-WR-TIMEZONE', 'America/Los_Angeles')
    ics.add('X-WR-CALDESC', 'Calendar of DUB seminars.')

    for seminar_path_current in seminar_paths:
        # Parse the seminar
        with open(seminar_path_current) as f:
            seminar_contents = list(yaml.safe_load_all(f))[0]

        # Add seminar as calendar event
        ics_event = Event()

        # Give it a UID
        ics_event.add(
            'UID',
            seminar_contents['date'].strftime('%Y-%m-%d') + '@dub.washington.edu'
        )

        # Give it DTSTART and DTEND
        timezone = pytz.timezone('America/Los_Angeles')
        seminar_start_time = timezone.localize(datetime.combine(
            seminar_contents['date'],
            datetime.strptime(seminar_contents['time'], '%I:%M %p').time()
        ))
        seminar_end_time = timezone.localize(datetime.combine(
            seminar_contents['date'],
            datetime.strptime(seminar_contents['time_end'], '%I:%M %p').time()
        ))
        ics_event.add('DTSTART', seminar_start_time)
        ics_event.add('DTEND', seminar_end_time)

        # Generate SUMMARY from applicable components
        if seminar_contents.get('no_seminar', False):
            # Flagged as not having a seminar

            # Title should indicate why there's no seminar
            seminar_summary = seminar_contents['title']
        else:
            # We have a seminar, but its data may not yet be complete
            seminar_summary = 'DUB Seminar'

            if not seminar_contents.get('tbd_speakers', False):
                # We have speakers

                # If they all have the same affiliation, we'll collapse it, so let's check
                speaker_affiliations = [
                    speaker_current['affiliation'] if not speaker_current.get('affiliation_none', False) else 'affiliation_none'
                    for speaker_current
                    in seminar_contents['speakers']
                ]
                if len(set(speaker_affiliations)) == 1:
                    # Everybody has the same affiliation
                    # But it's still possible that affiliation is affiliation_none
                    if not seminar_contents['speakers'][0].get('affiliation_none', False):
                        # We have a legit affiliation
                        seminar_summary = '{} - {} ({})'.format(
                            seminar_summary,
                            ', '.join(
                                [
                                    ' '.join(speaker_current['name'][1:] + [speaker_current['name'][0]])
                                    for speaker_current
                                    in seminar_contents['speakers']
                                ]
                            ),
                            seminar_contents['speakers'][0]['affiliation']
                        )
                    else:
                        # Everybody has no affiliation
                        seminar_summary = '{} - {}'.format(
                            seminar_summary,
                            ', '.join(
                                [
                                    ' '.join(speaker_current['name'][1:] + [speaker_current['name'][0]])
                                    for speaker_current
                                    in seminar_contents['speakers']
                                ]
                            )
                        )
                else:
                    # Distinct affiliations
                    seminar_summary = '{} - {}'.format(
                        seminar_summary,
                        ', '.join(
                            [
                                '{}{}'.format(
                                    ' '.join(speaker_current['name'][1:] + [speaker_current['name'][0]]),
                                    '({})'.format(speaker_current['affiliation']) if not speaker_current.get('affiliation_none', False) else ''
                                )
                                for speaker_current
                                in seminar_contents['speakers']
                            ]
                        )
                    )
            else:
                # No speakers yet
                seminar_summary = '{} - TBD'.format(
                    seminar_summary
                )

            if not seminar_contents.get('tbd_title', False):
                # We have a title
                seminar_summary = '{} - "{}"'.format(
                    seminar_summary,
                    seminar_contents['title']
                )

        ics_event.add('SUMMARY', seminar_summary)

        # Add the location unless it has an override
        if seminar_contents.get('location_override_calendar', False):
            ics_event.add('LOCATION', seminar_contents['location_override_calendar'])
        else:
            ics_event.add('LOCATION', seminar_contents['location'])

        # This description generation is still a bit sketchy, should decide what we want
        #
        # Generate description string from applicable components
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

        # Parse description as markdown
        class SensibleParagraphs(markdown.extensions.Extension):
            def extendMarkdown(self, md, md_globals):
                br_tag = markdown.inlinepatterns.SubstituteTagPattern(r'\n', None)
                md.inlinePatterns.add('nl', br_tag, '_end')

        ics_event.add('DESCRIPTION', markdown.markdown(description_string, extensions=[SensibleParagraphs()]))

        ics.add_component(ics_event)

    # Store the ics file output
    with open('calendar.ics', 'wb') as f:
        f.write(ics.to_ical())


@invoke.task(pre=[update_dependencies])
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

        # Regardless of platform we're on, standardize the path we store (e.g., slashes)
        seminar_path_stored = posixpath.join(*os.path.normpath(seminar_path_current).split(os.sep))

        if seminar_path_stored not in seminar_calendar_sequences:
            seminar_calendar_sequences[seminar_path_stored] = {
                'hash': seminar_hash_current,
                'sequence': seminar_sequence_current
            }

        seminar_hash_stored = seminar_calendar_sequences[seminar_path_stored]['hash']
        seminar_sequence_stored = seminar_calendar_sequences[seminar_path_stored]['sequence']

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

        seminar_calendar_sequences[seminar_path_stored] = {
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


@invoke.task(pre=[update_dependencies])
def compile_requirements():
    # Compile the requirements file
    invoke.run(
        'pip-compile --upgrade --output-file requirements3.txt requirements3.in',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[update_dependencies, compile_calendar])
def build_production():
    invoke.run(
        'bundle exec jekyll build -t --config _config.yml,_config-production.yml',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[update_dependencies, compile_calendar])
def build_test():
    invoke.run(
        'bundle exec jekyll build -t --config _config.yml,_config-test.yml',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[update_dependencies, compile_calendar])
def serve_production():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-production.yml -H 0.0.0.0',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[update_dependencies, compile_calendar])
def serve_test():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-test.yml --watch --force_polling',
        encoding=sys.stdout.encoding
    )


@invoke.task
def update_base():
    invoke.run('git pull https://github.com/fogies/web-jekyll-base.git master', encoding=sys.stdout.encoding)
