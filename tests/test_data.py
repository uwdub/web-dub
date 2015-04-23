import os.path
import unittest
import yaml


class TestData(unittest.TestCase):
    def setUp(self) -> None:
        """
        Parse our data files and combine them into a dictionary.
        """
        data_files = [
            'authors',
            'conferencepapers',
            'conferences',
            'journalpapers',
            'journals',
            'workshoppapers',
            'workshops',
        ]

        self.data = {}
        for data_current in data_files:
            with open('_data/{}.yml'.format(data_current)) as f:
                self.data[data_current] = yaml.load(f)

    def test_parse_yaml(self) -> None:
        """
        Confirm all YAML from setUp successfully parses.
        """
        pass
