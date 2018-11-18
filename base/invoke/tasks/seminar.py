import jinja2
import os
import yaml
import invoke


@invoke.task()
def seminar_update_template():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(searchpath='_seminars'),
        trim_blocks=True,
        lstrip_blocks=True,
        undefined=jinja2.StrictUndefined
    )
    template = env.get_template('_template.md')

    seminar_paths = [
        seminar_file_entry.path
        for seminar_file_entry
        in os.scandir('_seminars')
        if (
            seminar_file_entry.is_file()
            and seminar_file_entry.name != '_template.md'
        )
    ]

    for seminar_path_current in seminar_paths:
        # Load the existing seminar file
        with open(seminar_path_current, encoding='utf-8') as f:
            # Parse the YAML of the seminar
            seminar = list(yaml.safe_load_all(f))[0]

            # If we ever have more than one version, we'll need to check things here
            assert seminar['version'] == 1

        # Write it back using the template
        seminar_rendered = template.render(seminar)
        with open(seminar_path_current, encoding='utf-8', mode='w') as f:
            f.write(seminar_rendered)
