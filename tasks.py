import invoke


@invoke.task
def update_dependencies():
    invoke.run('gem install bundler')
    invoke.run('bundle install')
    invoke.run('npm install')
    invoke.run('pip install -r requirements3.txt')


@invoke.task(pre=[update_dependencies])
def build():
    invoke.run('bundle exec jekyll build -t --config _config.yml')


@invoke.task(pre=[update_dependencies])
def serve():
    invoke.run('bundle exec jekyll serve -t --config _config.yml,_config-serve.yml --watch --force_polling --incremental')


@invoke.task
def update_base():
    invoke.run('git pull https://github.com/fogies/web-jekyll-base.git master')
