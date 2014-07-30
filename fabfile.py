import fabric
import fabric.api

fabric.api.env.hosts = ['barb.cs.washington.edu']
fabric.api.env.user = 'jfogarty'


def build():
    fabric.api.local('jekyll build --config _config.yml')


def deploy():
    # Locally build the website
    fabric.api.local('jekyll build --config _config.yml')

    # Ensure the server has our staging directory
    fabric.api.run('mkdir -p ~/fabric_staging/web-jayfo/')

    # Ensure the staging directory is empty
    fabric.api.run('rm -rf ~/fabric_staging/web-jayfo/*')

    # Push up to the server staging directory
    fabric.api.put('_site/*', '~/fabric_staging/web-jayfo/')

    # And sync into the deployment directory
    fabric.api.run('rsync -r -c --delete ~/fabric_staging/web-jayfo/ ~/public_html/')


def serve():
    fabric.api.local('jekyll serve --config _config.yml,_config-dev.yml --watch --force_polling')


# We cannot have a test because Fabric requires Python 2.7 but our tests use Python 3.4
#
# def test():
#    fabric.api.local('nosetests')
