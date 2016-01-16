import invoke
import sys


@invoke.task
def update_dependencies():
    # The npm install command sometimes outputs characters that cause Unicode
    # errors on Windows, so we set the encoding parameter on our commands
    print('Updating Node.js dependencies')
    invoke.run('npm install', encoding=sys.stdout.encoding)

    # Python dependencies
    print('Updating Python dependencies')

    # TODO verify python version

    # Ensure we have a current version of pip, as needed by pip-tools
    # TODO check version that is installed
    result = invoke.run('pip show pip', encoding=sys.stdout.encoding, warn=True)
    invoke.run('pip install --upgrade pip', encoding=sys.stdout.encoding)

    # Ensure we have pip-tools
    # TODO check version that is installed
    result = invoke.run('pip show pip-tools', encoding=sys.stdout.encoding, warn=True)
    invoke.run('pip install pip-tools==1.4.2', encoding=sys.stdout.encoding)

    # pip-sync does not respect options in the requirements file, this ensure it only needs to delete
    invoke.run('pip install -r requirements3.txt', encoding=sys.stdout.encoding)
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
