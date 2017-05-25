import base.invoke.tasks.command
import base.invoke.tasks.compile
import invoke
import re
import sys
import yaml


@invoke.task
def update_base():
    invoke.run('git pull https://github.com/fogies/invoke-base.git master', encoding=sys.stdout.encoding)


@invoke.task(pre=[
    base.invoke.tasks.compile.compile_config
])
def update_dependencies():
    # Parse our config
    with open('_base_config.yml') as f:
        base_config_yaml = yaml.safe_load(f)

    # Python dependencies
    print('Checking Python dependencies')

    # Ensure we have a current version of pip (e.g., as needed by pip-tools)
    pip_version_desired = base_config_yaml['config']['python']['pip_version']
    command = 'pip --disable-pip-version-check show pip'
    result = base.invoke.tasks.command.run(command)

    pip_version_current = re.search('^Version: ([\d.]+)', result.stdout, re.MULTILINE).group(1)
    if pip_version_current != pip_version_desired:
        command = 'python -m pip install --upgrade pip=={}'.format(
            pip_version_desired
        )
        result = base.invoke.tasks.command.run(command)

    # Ensure we have pip-tools, which will be in our requirements file
    # pip-sync also currently does not respect options in the requirements file,
    # so installing the entire file ensures pip-sync only needs to delete
    command = 'pip --disable-pip-version-check install -r requirements3.txt'
    result = base.invoke.tasks.command.run(command)
    # Ensure we have exactly our dependencies
    command = 'pip-sync requirements3.txt'
    result = base.invoke.tasks.command.run(command)

    # Node dependencies
    if base_config_yaml['config'].get('node', {}).get('required', False):
        print('Checking Node.js dependencies')

        command = 'npm install'
        result = base.invoke.tasks.command.run(command)

    # Ruby dependencies
    if base_config_yaml['config'].get('ruby', {}).get('required', False):
        print('Checking Ruby dependencies')

        # Check we have the correct Bundler version
        bundler_version_desired = base_config_yaml['config']['ruby']['bundler_version']
        command = 'gem list -i bundler -v {}'.format(
            bundler_version_desired
        )
        result = base.invoke.tasks.command.run(command, error_on_failure=False)

        # Expected to fail if the desired version is not installed
        if result.failed:
            command = 'gem install bundler -v {}'.format(
                bundler_version_desired
            )
            result = base.invoke.tasks.command.run(command)

        # And only the correct Bundler version
        # Expected to fail if no other versions of bundler are installed
        command = 'gem uninstall bundler -v "!={}"'.format(
            bundler_version_desired
        )
        result = base.invoke.tasks.command.run(command, error_on_failure=False)

        # Check we have our Ruby dependencies
        command = 'bundle check'
        result = base.invoke.tasks.command.run(command, error_on_failure=False)

        # Expected to fail if we are missing dependencies
        if result.failed:
            command = 'bundle install'
            result = base.invoke.tasks.command.run(command)
