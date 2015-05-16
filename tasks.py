import invoke


@invoke.task
def build():
    invoke.run('jekyll build --config _config.yml,_config-dev.yml')


@invoke.task
def serve():
    invoke.run('jekyll serve --config _config.yml,_config-dev.yml --watch --force_polling')
