import base.docker
import nose.tools
import requests
import yaml


class TestConnect:
    @classmethod
    def setup_class(cls):
        # Parse our compile config
        with open('_base_config.yml') as f:
            TestConnect.base_config = yaml.safe_load(f)['config']

    def test_connect_to_nginx(self):
        if TestConnect.base_config['docker']['required']:
            response = requests.get(
                'http://{}:{}'.format(
                    base.docker.machine_ip(),
                    80
                )
            )

            nose.tools.assert_equals(
                response.status_code,
                200
            )
