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

    # Ensure we have pip-tools
    result = invoke.run('pip show pip-tools', encoding=sys.stdout.encoding, warn=True)
    if result.failed:
        invoke.run('pip install pip-tools', encoding=sys.stdout.encoding)

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
def build():
    invoke.run('bundle exec jekyll build -t --config _config.yml', encoding=sys.stdout.encoding)


@invoke.task(pre=[update_dependencies])
def serve():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-serve.yml --watch --force_polling',
        encoding=sys.stdout.encoding
    )


@invoke.task
def update_base():
    invoke.run('git pull https://github.com/fogies/web-jekyll-base.git master', encoding=sys.stdout.encoding)
