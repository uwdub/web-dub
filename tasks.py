import invoke
import sys


@invoke.task
def update_dependencies():
    # The npm install command sometimes outputs characters that cause Unicode
    # errors on Windows, so we set the encoding parameter
    print('Updating Node.js dependencies')
    invoke.run('npm install', encoding=sys.stdout.encoding)
    print('Updating Python dependencies')
    invoke.run('pip install -r requirements3.txt', encoding=sys.stdout.encoding)
    print('Updating Ruby dependencies')
    invoke.run('gem install bundler', encoding=sys.stdout.encoding)
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
