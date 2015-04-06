import fabric
import fabric.api

fabric.api.env.hosts = ['barb.cs.washington.edu']
fabric.api.env.user = 'jfogarty'


def build():
    fabric.api.local('jekyll build --config _config.yml')


# Our deploy now happens via GitHub
#
# def deploy():
#     pass

def serve():
    fabric.api.local('jekyll serve --config _config.yml,_config-dev.yml --watch --force_polling')


# We cannot have a test because Fabric requires Python 2.7 but our tests use Python 3.4
#
# def test():
#    fabric.api.local('nosetests')
