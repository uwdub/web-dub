import os.path
import re
import unittest
import yaml


class TestWorkshopPapers(unittest.TestCase):
    def setUp(self) -> None:
        """
        Parse our data files and combine them into a dictionary.
        """
        data_files = [
            'authors',
            'workshoppapers',
            'workshops'
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

    def test_workshops_id_unique(self) -> None:
        """
        Confirm every workshop id is unique.

        The YAML parser does not error on this, and just keeps the most recently parsed.

        So we need to look at the file ourself.
        """
        with open('_data/workshops.yml') as f:
            id_existing = set()
            for line in f:
                match = re.match('(id_workshop_.*):', line)
                if match:
                    id_workshop = match.group(1)

                    self.assertNotIn(
                        id_workshop,
                        id_existing,
                        '{} is duplicated in workshops.yml'.format(id_workshop)
                    )

                    id_existing.add(id_workshop)

            self.assertGreater(
                len(id_existing),
                0,
                'No ID were parsed in workshops.yml'
            )

    def test_workshoppapers_authors_exist(self) -> None:
        """
        Confirm all authors referenced by a paper actually exist.
        """
        for id_workshoppaper, workshoppaper in self.data['workshoppapers'].items():
            for id_author in workshoppaper['authors']:
                self.assertIn(
                    id_author,
                    self.data['authors'],
                    '{} references author {} not found in authors.yml'.format(id_workshoppaper, id_author)
                )

    def test_workshoppapers_workshop_exist(self) -> None:
        """
        Confirm all workshops referenced by a paper actually exist.
        """
        for id_workshoppaper, workshoppaper in self.data['workshoppapers'].items():
            id_workshop = workshoppaper['workshop']
            self.assertIn(
                id_workshop,
                self.data['workshops'],
                '{} references workshop {} not found in workshops.yml'.format(id_workshoppaper, id_workshop)
            )

    def test_workshoppapers_files_exist(self) -> None:
        """
        Confirm all files references by a paper actually exist.
        """
        for id_workshoppaper, workshoppaper in self.data['workshoppapers'].items():
            # Papers may have a PDF
            if 'localpdf' in workshoppaper:
                file_path = workshoppaper['localpdf']
                self.assertTrue(
                    os.path.isfile('publications/{}'.format(file_path)),
                    '{} references localpdf {} not found in publications/'.format(id_workshoppaper, file_path)
                )

    def test_workshoppapers_id_unique(self) -> None:
        """
        Confirm every workshoppaper id is unique.

        The YAML parser does not error on this, and just keeps the most recently parsed.

        So we need to look at the file ourself.
        """
        with open('_data/workshoppapers.yml') as f:
            id_existing = set()
            for line in f:
                match = re.match('(id_workshoppaper_.*):', line)
                if match:
                    id_workshoppaper = match.group(1)

                    self.assertNotIn(
                        id_workshoppaper,
                        id_existing,
                        '{} is duplicated in workshoppapers.yml'.format(id_workshoppaper)
                    )

                    id_existing.add(id_workshoppaper)

            self.assertGreater(
                len(id_existing),
                0,
                'No ID were parsed in workshoppapers.yml'
            )
