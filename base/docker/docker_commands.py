import os
import subprocess
import sys
import yaml


def compose_up(file_compose, service):
    compose_run(file_compose, 'build {}'.format(service))
    compose_run(file_compose, 'up -d {}'.format(service))


def compose_run(file_compose, compose_command):
    # Parse our config
    with open('_base_config.yml') as f:
        config_yaml = yaml.safe_load(f)

    # Assemble our command according to our OS
    if 'BASE_DOCKER_ON_TRAVIS' in os.environ:
        command = 'docker-compose -f "{}" {}'.format(
            file_compose,
            compose_command
        )
    elif sys.platform == 'darwin':
        command = '"{}" "{}" docker-compose -f "{}" {}'.format(
            config_yaml['config']['docker']['toolbox']['macos']['cmd_bash'],
            os.path.normpath(os.path.join(os.getcwd(), 'base/docker/docker_bash.sh')).replace('\\', '/'),
            os.path.normpath(os.path.join(os.getcwd(), file_compose)).replace('\\', '/'),
            compose_command
        )
    elif sys.platform == 'win32':
        command = '"{}" "{}" docker-compose -f "{}" {}'.format(
            config_yaml['config']['docker']['toolbox']['windows']['cmd_bash'],
            os.path.normpath(os.path.join(os.getcwd(), 'base/docker/docker_bash.sh')).replace('\\', '/'),
            os.path.normpath(os.path.join(os.getcwd(), file_compose)).replace('\\', '/'),
            compose_command
        )
    else:
        raise Exception('Unknown runtime environment')

    # Call the command
    process = subprocess.Popen(
        command,
        shell=True,
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,
        # universal_newlines=True
    )
    # for line in process.stdout:
    #     flag_print = line.startswith('Step ')
    #
    #     if flag_print:
    #         print(line, end='', flush=True)


# def docker_run(docker_command, check_result=True):
def docker_run(docker_command):
    # Parse our config
    with open('_base_config.yml') as f:
        config_yaml = yaml.safe_load(f)

    # Assemble our command according to our OS
    if 'BASE_DOCKER_ON_TRAVIS' in os.environ:
        command = 'docker {}'.format(
            docker_command
        )
    elif sys.platform == 'darwin':
        command = '"{}" "{}" docker {}'.format(
            config_yaml['config']['docker']['toolbox']['macos']['cmd_bash'],
            os.path.normpath(os.path.join(os.getcwd(), 'base/docker/docker_bash.sh')).replace('\\', '/'),
            docker_command
        )
    elif sys.platform == 'win32':
        command = '"{}" "{}" docker {}'.format(
            config_yaml['config']['docker']['toolbox']['windows']['cmd_bash'],
            os.path.normpath(os.path.join(os.getcwd(), 'base/docker/docker_bash.sh')).replace('\\', '/'),
            docker_command
        )
    else:
        raise Exception('Unknown runtime environment')

    # Call the command
    result = subprocess.run(
        command,
        # shell=True,
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE
    )
    # if check_result:
    #     _check_result(command, result)
    #
    # return result


def machine_console():
    # Parse our config
    with open('_base_config.yml') as f:
        config_yaml = yaml.safe_load(f)

    # Assemble our command according to our OS
    if sys.platform == 'darwin':
        command = '"{}" "{}"'.format(
            config_yaml['config']['docker']['toolbox']['macos']['cmd_bash'],
            os.path.normpath(os.path.join(os.getcwd(), 'base/docker/docker_console.sh')).replace('\\', '/')
        )
    elif sys.platform == 'win32':
        command = 'cmd /c start "{}" "{}"'.format(
            config_yaml['config']['docker']['toolbox']['windows']['cmd_bash'],
            os.path.normpath(os.path.join(os.getcwd(), 'base/docker/docker_console.sh')).replace('\\', '/')
        )
    else:
        raise Exception('Unknown runtime environment')

    # Call the command, noting that this cannot be piped
    subprocess.run(
        command,
        shell=True
    )


def machine_ensure():
    # On Travis, docker is already available
    if 'BASE_DOCKER_ON_TRAVIS' in os.environ:
        return

    # Parse our config
    with open('_base_config.yml') as f:
        config_yaml = yaml.safe_load(f)

    # Assemble our command according to our OS
    if sys.platform == 'darwin':
        command = '"{}" "{}"'.format(
            config_yaml['config']['docker']['toolbox']['macos']['cmd_bash'],
            os.path.normpath(os.path.join(
                os.getcwd(),
                'base/docker/docker_ensure_machine.sh'
            )).replace('\\', '/')
        )
    elif sys.platform == 'win32':
        command = '"{}" "{}"'.format(
            config_yaml['config']['docker']['toolbox']['windows']['cmd_bash'],
            os.path.normpath(os.path.join(
                os.getcwd(),
                'base/docker/docker_ensure_machine.sh'
            )).replace('\\', '/')
        )
    else:
        raise Exception('Unknown runtime environment')

    # Call the command
    result = subprocess.run(
        command,
        shell=True,
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE
    )
    # _check_result(command, result)


def machine_ip():
    # On Travis, docker is already available
    if 'BASE_DOCKER_ON_TRAVIS' in os.environ:
        return 'localhost'

    # Parse our config
    with open('_base_config.yml') as f:
        config_yaml = yaml.safe_load(f)

    # Assemble our command according to our OS
    if sys.platform == 'darwin':
        command = '"{}" ip default'.format(
            config_yaml['config']['docker']['toolbox']['macos']['cmd_dockermachine']
        )
    elif sys.platform == 'win32':
        command = '"{}" ip default'.format(
            config_yaml['config']['docker']['toolbox']['windows']['cmd_dockermachine']
        )
    else:
        raise Exception('Unknown runtime environment')

    # Call the command
    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # _check_result(command, result)

    ip_address = result.stdout.decode('utf-8', 'backslashreplace').strip()

    return ip_address
