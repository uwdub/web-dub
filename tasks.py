import invoke
import sys


@invoke.task
def update_dependencies():
    # The npm install command sometimes outputs characters that cause Unicode
    # errors on Windows, so we hide the output and print our own simple messages
    #
    # Setting the encoding parameter also works, done here in case the hide is removed
    print('Updating Node.js dependencies')
    invoke.run('npm install', encoding=sys.stdout.encoding, hide=True)
    print('Updating Python dependencies')
    invoke.run('pip install -r requirements3.txt', hide=True)
    print('Updating Ruby dependencies')
    invoke.run('gem install bundler', hide=True)
    invoke.run('bundle install', hide=True)


@invoke.task(pre=[update_dependencies])
def build():
    invoke.run('bundle exec jekyll build -t --config _config.yml')


@invoke.task(pre=[update_dependencies])
def serve():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-serve.yml --watch --force_polling --incremental'
    )


@invoke.task
def update_base():
    invoke.run('git pull https://github.com/fogies/web-jekyll-base.git master')
