import invoke
import jinja2
import re
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
