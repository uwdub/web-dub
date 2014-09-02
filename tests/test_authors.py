import os.path
import unittest
import yaml


class TestConferencePapers(unittest.TestCase):
    def setUp(self) -> None:
        """
        Parse our data files and combine them into a dictionary.
        """
        data_files = [
            'authors'
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

    def test_authors_id_format(self) -> None:
        """
        Confirm the author id is in the expected format.
        """
        for id_author, author in self.data['authors'].items():
            if 'id_override' in author:
                id_expected = author['id_override']
            else:
                id_expected = 'id_author_{}_{}'.format(
                    author['name'][0].lower().replace(' ', '_'),
                    author['name'][1].lower().replace(' ', '_')
                )

            self.assertEquals(
                id_author,
                id_expected,
                '{} does not have expected id {}'.format(id_author, id_expected)
            )
