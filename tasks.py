import hashlib
import invoke
import jinja2
import re
import os
import sys
import yaml


@invoke.task
def update_dependencies():
    # Parse our compile config
    with open('_compile-config.yml') as f:
        compile_config = yaml.safe_load(f)

    # The npm install command sometimes outputs characters that cause Unicode
    # errors on Windows, so we set the encoding parameter on our commands
    print('Updating Node.js dependencies')
    invoke.run('npm install', encoding=sys.stdout.encoding)

    # Python dependencies
    print('Updating Python dependencies')

    # Ensure we have a current version of pip, as needed by pip-tools
    version_desired = compile_config['config']['pip_version']
    result = invoke.run('pip --disable-pip-version-check show pip', encoding=sys.stdout.encoding, warn=True)
    version_current = re.search('^Version: ([\d\.]+)', result.stdout, re.MULTILINE).group(1)
    if version_current != version_desired:
        invoke.run(
            'python -m pip install --upgrade pip=={}'.format(
                version_desired
            ),
            encoding=sys.stdout.encoding
        )

    # Ensures we have pip-tools
    # pip-sync also does not respect options in the requirements file, so this ensures pip-sync only needs to delete
    invoke.run('pip --disable-pip-version-check install -r requirements3.txt', encoding=sys.stdout.encoding)
    # Ensure we have exactly our dependencies
    invoke.run('pip-sync requirements3.txt', encoding=sys.stdout.encoding)

    # Ruby dependencies
    print('Updating Ruby dependencies')

    # Check we have the correct Bundler version
    result = invoke.run('gem list -i bundler -v 1.10.6', encoding=sys.stdout.encoding, warn=True)
    if result.failed:
        invoke.run('gem install bundler -v 1.10.6', encoding=sys.stdout.encoding)

    # And only the correct Bundler version
    invoke.run('gem uninstall bundler -v "!=1.10.6"', encoding=sys.stdout.encoding, warn=True)

    # List our bundler installs
    invoke.run('gem list bundler', encoding=sys.stdout.encoding, warn=True)

    # Check we have our Ruby dependencies
    result = invoke.run('bundle check', encoding=sys.stdout.encoding, warn=True)
    if result.failed:
        invoke.run('bundle install', encoding=sys.stdout.encoding)


@invoke.task(pre=[update_dependencies])
def build_production():
    invoke.run('bundle exec jekyll build -t --config _config.yml,_config-build-production.yml', encoding=sys.stdout.encoding)


@invoke.task(pre=[update_dependencies])
def build_test():
    invoke.run('bundle exec jekyll build -t --config _config.yml,_config-build-test.yml', encoding=sys.stdout.encoding)


@invoke.task()
def compile_config():
    # Parse our compile config
    with open('_compile-config.yml') as f:
        compile_config = yaml.safe_load(f)

    # Compile each jinja2 file
    for jinja2_entry in compile_config['jinja2']['entries']:
        jinja2_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath='.'))
        template = jinja2_environment.get_template(jinja2_entry['in'])
        with open(jinja2_entry['out'], 'w') as f:
            f.write(template.render(compile_config['config']))


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

    for seminar_path_current in seminar_paths:
        # Get the hash and sequence from the file, to compare against our stored data
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

    # Store our updated sequences
    data = {'sequences': seminar_calendar_sequences }
    with open('_compile-calendar-sequences.yml', 'w') as f:
        yaml.dump(
            data,
            stream=f,
            default_flow_style=False
        )


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


@invoke.task(pre=[update_dependencies])
def serve_production():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-serve-production.yml -H 0.0.0.0',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[update_dependencies])
def serve_test():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-serve-test.yml --watch --force_polling',
        encoding=sys.stdout.encoding
    )


@invoke.task
def update_base():
    invoke.run('git pull https://github.com/fogies/web-jekyll-base.git master', encoding=sys.stdout.encoding)
