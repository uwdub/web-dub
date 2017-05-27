import base.docker
import invoke
import jinja2
import os
import yaml


@invoke.task()
def docker_machine_ensure():
    base.docker.machine_ensure()


@invoke.task(pre=[docker_machine_ensure])
def docker_console():
    base.docker.machine_console()


@invoke.task(pre=[docker_machine_ensure])
def docker_ip():
    print(base.docker.machine_ip())


@invoke.task(pre=[docker_machine_ensure])
def docker_localize():
    # Parse our config
    with open('_base_config.yml') as f:
        config_yaml = yaml.safe_load(f)

    # Compile files that need their docker-related information localized
    for jinja2_entry in config_yaml['compile_docker_localize']['entries']:
        jinja2_environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(searchpath='.'),
            undefined=jinja2.StrictUndefined
        )
        template = jinja2_environment.get_template(jinja2_entry['in'])
        with open(jinja2_entry['out'], 'w') as f:
            f.write(template.render({
                'DOCKER_LOCALIZE_CWD': os.path.normpath(os.getcwd()).replace('\\', '/'),
                'DOCKER_LOCALIZE_IP': base.docker.machine_ip()
            }))


@invoke.task(pre=[docker_localize])
def docker_start():
    base.docker.compose_run('tests/full/docker/test_compose.localized.yml', 'build')
    base.docker.compose_run('tests/full/docker/test_compose.localized.yml', 'up -d')


@invoke.task(pre=[docker_localize])
def docker_stop():
    base.docker.compose_run('tests/full/docker/test_compose.localized.yml', 'stop')
