import invoke


@invoke.task
def update_dependencies():
    print('Updating dependencies')
    invoke.run('bundle install')
    invoke.run('pip install -r requirements3.txt')


@invoke.task(pre=[update_dependencies])
def build():
    invoke.run('bundle exec jekyll build -t --config _config.yml,_config-dev.yml')


@invoke.task(pre=[update_dependencies])
def serve():
    invoke.run('bundle exec jekyll serve -t --config _config.yml,_config-dev.yml --watch --force_polling')


@invoke.task
def update_base():
    invoke.run('git pull https://github.com/fogies/web-jekyll-base.git master')
