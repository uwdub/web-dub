import base.invoke.tasks.update
import invoke
import sys


@invoke.task(pre=[base.invoke.tasks.update.update_dependencies])
def build_production():
    invoke.run(
        'bundle exec jekyll build -t --config _config.yml,_config-production.yml',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[base.invoke.tasks.update.update_dependencies])
def build_test():
    invoke.run(
        'bundle exec jekyll build -t --config _config.yml,_config-test.yml',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[base.invoke.tasks.update.update_dependencies])
def serve_production():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-production.yml -H 0.0.0.0',
        encoding=sys.stdout.encoding
    )


@invoke.task(pre=[base.invoke.tasks.update.update_dependencies])
def serve_test():
    invoke.run(
        'bundle exec jekyll serve -t --config _config.yml,_config-test.yml --watch --force_polling',
        encoding=sys.stdout.encoding
    )
