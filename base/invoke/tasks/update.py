import invoke
import sys


@invoke.task
def update_base():
    invoke.run('git pull https://github.com/fogies/invoke-base.git master', encoding=sys.stdout.encoding)
