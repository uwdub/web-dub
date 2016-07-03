import cloudinary
import cloudinary.uploader
import cloudinary.utils
import hashlib
import invoke
import jinja2
import re
import os
import sys
import requests
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


@invoke.task()
def compile_people_images():
    # Obtain our stored people data
    with open('_compile-people-images.yml') as f:
        people = yaml.safe_load(f)['people']

    # Iterate over all our people files
    people_paths = []
    for people_root_entry, people_dir_entries, people_file_entries in os.walk('_people'):
        # Skip the images directories
        if '_images_raw' in people_dir_entries:
            people_dir_entries.remove('_images_raw')
        # Skip the unchecked directories
        if '_unchecked' in people_dir_entries:
            people_dir_entries.remove('_unchecked')
        # Skip any template files
        if 'template.md' in people_file_entries:
            people_file_entries.remove('template.md')

        # Keep only .md files
        people_file_entries = [
            people_file_current
            for people_file_current
            in people_file_entries
            if os.path.splitext(people_file_current)[1] == '.md'
        ]

        for file_entry_current in people_file_entries:
            people_paths.append(
                os.path.normpath(
                    os.path.join(people_root_entry, file_entry_current)
                )
            )

    # Go through the corresponding images
    for people_path_current in people_paths:
        # Get a base without the extension
        people_path_current_base = os.path.splitext(people_path_current)[0]
        # Convert that into an image base
        people_path_current_image_raw_base = os.path.join(
            os.path.split(people_path_current_base)[0],
            '_images_raw',
            os.path.split(people_path_current_base)[1]
        )
        people_path_current_image_normalized = os.path.join(
            people_path_current_base + '.jpg'
        )

        # Check if a corresponding image exists
        people_path_current_image_raw = None
        if os.path.exists(people_path_current_image_raw_base + '.jpg'):
            people_path_current_image_raw = people_path_current_image_raw_base + '.jpg'
        elif os.path.exists(people_path_current_image_raw_base + '.png'):
            people_path_current_image_raw = people_path_current_image_raw_base + '.png'

        # If we have an image for this person, check whether it needs normalized
        if people_path_current_image_raw:
            # Handle a case where this is a new person
            if people_path_current not in people:
                people[people_path_current] = {
                    'image_hash': '',
                }

            # Our parameters are part of the hash
            params_cloudinary = {
                'width': 150,
                'height': 150,
                'crop': 'thumb',
                'gravity': 'auto'
            }

            # Get the hash from the file, to compare against our stored data
            md5 = hashlib.md5()
            md5.update(repr(sorted(params_cloudinary.items())).encode('utf-8'))
            with open(people_path_current_image_raw, 'rb') as f:
                md5.update(f.read())
            image_hash_current = md5.hexdigest()

            # Get the hash we have previously processed
            image_hash_stored = people[people_path_current]['image_hash']

            # If the image has changed, we need to process it
            if image_hash_current != image_hash_stored:
                # Normalizing will require Cloudinary
                if os.path.exists('secrets/cloudinary.yml'):
                    with open('secrets/cloudinary.yml') as f:
                        secrets_cloudinary = yaml.safe_load(f)['secrets']

                    cloudinary.config(
                        cloud_name=secrets_cloudinary['cloud_name'],
                        api_key=secrets_cloudinary['api_key'],
                        api_secret=secrets_cloudinary['api_secret'],
                    )

                    cloudinary_image_id = os.path.split(people_path_current_base)[1]

                    cloudinary.uploader.upload(
                        people_path_current_image_raw,
                        public_id=cloudinary_image_id
                    )

                    cloudinary_image_url = cloudinary.utils.cloudinary_url(
                        cloudinary_image_id,
                        **params_cloudinary
                    )[0]

                    # Download the image
                    response = requests.get(cloudinary_image_url, stream=True)
                    with open(people_path_current_image_normalized, 'wb') as f:
                        f.write(response.content)

                    # Store the hash we used to compute this
                    people[people_path_current] = {
                        'image_hash': image_hash_current,
                    }

    # Store our updated people
    data = {'people': people}
    with open('_compile-people-images.yml', 'w') as f:
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
