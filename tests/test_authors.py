import re
import unittest
import yaml


class TestAuthors(unittest.TestCase):
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
                id_expected = 'id_author_{}'.format(
                    author['id_override']
                )
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

    def test_authors_id_unique(self) -> None:
        """
        Confirm every author id is unique.

        The YAML parser does not error on this, and just keeps the most recently parsed.

        So we need to look at the file ourself.
        """
        with open('_data/authors.yml') as f:
            id_existing = set()
            for line in f:
                match = re.match('(id_author_.*):', line)
                if match:
                    id_author = match.group(1)

                    self.assertNotIn(
                        id_author,
                        id_existing,
                        '{} is duplicated in authors.yml'.format(id_author)
                    )

                    id_existing.add(id_author)

            self.assertGreater(
                len(id_existing),
                0,
                'No ID were parsed in authors.yml'
            )

