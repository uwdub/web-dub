import invoke
import jinja2
import sys
import yaml


@invoke.task()
def compile_config():
    # Parse our compile config
    with open('_base_config.yml') as f:
        base_config_yaml = yaml.safe_load(f)

    # Compile each jinja2 file
    for jinja2_entry in base_config_yaml['compile_config']['entries']:
        jinja2_environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(searchpath='.'),
            trim_blocks=True,
            undefined=jinja2.StrictUndefined
        )
        template = jinja2_environment.get_template(jinja2_entry['in'])
        with open(jinja2_entry['out'], 'w') as f:
            f.write(template.render(base_config_yaml['config']))


@invoke.task(pre=[compile_config])
def compile_requirements():
    # Compile the requirements file
    invoke.run(
        'pip-compile --upgrade --output-file requirements3.txt requirements3.in',
        encoding=sys.stdout.encoding
    )
