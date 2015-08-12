import subprocess
import unittest


class TestBuild(unittest.TestCase):
    def test_build(self):
        self.assertEqual(
            subprocess.call('jekyll build --config _config.yml', shell=True),
            0,
            'Jekyll build failed'
        )

