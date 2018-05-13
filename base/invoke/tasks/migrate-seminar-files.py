#
# migrate-seminar-files.py
#
# Read all existing seminar files, gather their data, and run them
# through a Jinja2 template for re-rendering.
#

import os
from io import StringIO
import yaml
import invoke
from jinja2 import Environment, FileSystemLoader

SOURCE_DIR = './_seminars/'
OUTPUT_DIR = './_seminars-new/'

@invoke.task()
def migrate_seminar_files():
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    env = Environment(
        loader=FileSystemLoader(searchpath='./_seminars'),
        trim_blocks=True,
        lstrip_blocks=True
    )
    template = env.get_template('_template.j2')

    for filename in os.listdir(SOURCE_DIR):
        if not filename.endswith('.md'):
            continue

        with open(os.path.join(SOURCE_DIR, filename), 'r') as infile:
            # Strip the first and last lines of the seminar files, which
            # contain the Jekyll frontmatter delimiters (i.e. '---').
            # Convert the result back to a stream so we can parse it with
            # yaml.load().
            seminar_data = yaml.load(StringIO(''.join(infile.readlines()[1:-1])))

            # Make sure the bio and abstract text are free of newlines after
            # yaml parsing.
            try:
                seminar_data['bio'] = seminar_data['bio'].replace('\n', ' ')
                seminar_data['abstract'] = seminar_data['abstract'].replace('\n', ' ')
            except KeyError:
                pass

            with open(os.path.join(OUTPUT_DIR, filename), 'w') as outfile:
                outfile.write(template.render(seminar_data))
                outfile.close()

            infile.close()
