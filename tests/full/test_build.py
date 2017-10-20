import nose.tools
import subprocess


class TestBuild:
    def test_build(self):
        nose.tools.assert_equals(
            subprocess.call('invoke build_test', shell=True),
            0,
            'Jekyll build failed'
        )

