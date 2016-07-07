import hashlib
import subprocess
import unittest
import yaml


class TestCompileConfig(unittest.TestCase):
    def test_compile_config(self):
        # Parse our compile config
        with open('_compile-config.yml') as f:
            compile_config = yaml.safe_load(f)

        # Hash each output file
        before_output_hashes = {}
        for jinja2_entry in compile_config['jinja2']['entries']:
            with open(jinja2_entry['out'], 'rb') as f:
                before_output_hashes[jinja2_entry['out']] = hashlib.md5(f.read()).hexdigest()

        # Run the compile_config
        self.assertEqual(
            subprocess.call('invoke compile_config', shell=True),
            0,
            'invoke compile_config failed'
        )

        # Re-hash each output file
        after_output_hashes = {}
        for jinja2_entry in compile_config['jinja2']['entries']:
            with open(jinja2_entry['out'], 'rb') as f:
                after_output_hashes[jinja2_entry['out']] = hashlib.md5(f.read()).hexdigest()

        # Confirm they all match
        for jinja2_entry in compile_config['jinja2']['entries']:
            self.assertEqual(
                before_output_hashes[jinja2_entry['out']],
                after_output_hashes[jinja2_entry['out']],
                'compile_config detected inconsistency between {} and {}'.format(
                    jinja2_entry['out'],
                    jinja2_entry['in']
                )
            )
