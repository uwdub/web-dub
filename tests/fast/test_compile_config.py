import hashlib
import nose.tools
import subprocess
import yaml


class TestCompileConfig:
    @classmethod
    def setup_class(cls):
        # Parse our compile config
        with open('_base_config.yml') as f:
            TestCompileConfig.base_config = yaml.safe_load(f)

    def test_compile_config(self):
        # Hash each output file
        before_output_hashes = {}
        for compile_config_entry in TestCompileConfig.base_config['compile_config']['entries']:
            with open(compile_config_entry['out'], 'rb') as f:
                before_output_hashes[compile_config_entry['out']] = hashlib.md5(f.read()).hexdigest()

        # Run the compile_config
        nose.tools.assert_equals(
            subprocess.call('invoke compile_config', shell=True),
            0,
            'invoke compile_config failed'
        )

        # Re-hash each output file
        after_output_hashes = {}
        for compile_config_entry in TestCompileConfig.base_config['compile_config']['entries']:
            with open(compile_config_entry['out'], 'rb') as f:
                after_output_hashes[compile_config_entry['out']] = hashlib.md5(f.read()).hexdigest()

        # Confirm they all match
        for compile_config_entry in TestCompileConfig.base_config['compile_config']['entries']:
            nose.tools.assert_equals(
                before_output_hashes[compile_config_entry['out']],
                after_output_hashes[compile_config_entry['out']],
                'compile_config detected inconsistency between {} and {}'.format(
                    compile_config_entry['out'],
                    compile_config_entry['in']
                )
            )
