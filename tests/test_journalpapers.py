import os.path
import re
import unittest
import yaml


class TestJournalPapers(unittest.TestCase):
    def setUp(self) -> None:
        """
        Parse our data files and combine them into a dictionary.
        """
        data_files = [
            'authors',
            'journalpapers',
            'journals'
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

    def test_journals_id_format(self) -> None:
        """
        Confirm the journal id is in the expected format.

        Many journals do not have good short names, so this format is pretty minimal.
        """
        for id_journal, journal in self.data['journals'].items():
            id_expected = 'id_journal_.*'

            self.assertTrue(
                re.match(id_expected, id_journal),
                '{} does not match expected id {}'.format(id_journal, id_expected)
            )

    def test_journals_id_unique(self) -> None:
        """
        Confirm every journal id is unique.

        The YAML parser does not error on this, and just keeps the most recently parsed.

        So we need to look at the file ourself.
        """
        with open('_data/journals.yml') as f:
            id_existing = set()
            for line in f:
                match = re.match('(id_journal_.*):', line)
                if match:
                    id_journal = match.group(1)

                    self.assertNotIn(
                        id_journal,
                        id_existing,
                        '{} is duplicated in journals.yml'.format(id_journal)
                    )

                    id_existing.add(id_journal)

            self.assertGreater(
                len(id_existing),
                0,
                'No ID were parsed in journals.yml'
            )

    def test_journalpapers_authors_exist(self) -> None:
        """
        Confirm all authors referenced by a paper actually exist.
        """
        for id_journalpaper, journalpaper in self.data['journalpapers'].items():
            for id_author in journalpaper['authors']:
                self.assertIn(
                    id_author,
                    self.data['authors'],
                    '{} references author {} not found in authors.yml'.format(id_journalpaper, id_author)
                )

    def test_journalpapers_journal_exist(self) -> None:
        """
        Confirm all journals referenced by a paper actually exist.
        """
        for id_journalpaper, journalpaper in self.data['journalpapers'].items():
            id_journal = journalpaper['journal']
            self.assertIn(
                id_journal,
                self.data['journals'],
                '{} references journal {} not found in journals.yml'.format(id_journalpaper, id_journal)
            )

    def test_journalpapers_files_exist(self) -> None:
        """
        Confirm all files references by a paper actually exist.
        """
        for id_journalpaper, journalpaper in self.data['journalpapers'].items():
            # Every paper must have a thumb
            self.assertIn(
                'localthumb',
                journalpaper,
                '{} missing field localthumb'.format(id_journalpaper)
            )
            file_path = journalpaper['localthumb']
            self.assertTrue(
                os.path.isfile('publications/{}'.format(file_path)),
                '{} references localthumb {} not found in publications/'.format(id_journalpaper, file_path)
            )

            # Papers may have a PDF
            if 'localpdf' in journalpaper:
                file_path = journalpaper['localpdf']
                self.assertTrue(
                    os.path.isfile('publications/{}'.format(file_path)),
                    '{} references localpdf {} not found in publications/'.format(id_journalpaper, file_path)
                )

    def test_journalpapers_files_paths(self) -> None:
        """
        Confirm all files have paths that correspond to the ID.
        """
        for id_journalpaper, journalpaper in self.data['journalpapers'].items():
            # This will be the prefix for everything
            id_path = re.match('id_journalpaper_(.*)', id_journalpaper).group(1)

            # Every paper must have a thumb
            path_expected = '{}.png'.format(id_path)
            self.assertEquals(
                journalpaper['localthumb'],
                path_expected,
                '{} localthumb does not have expected path {}'.format(id_journalpaper, path_expected)
            )

            # Papers may have a PDF
            if 'localpdf' in journalpaper:
                path_expected = '{}.pdf'.format(id_path)
                self.assertEquals(
                    journalpaper['localpdf'],
                    path_expected,
                    '{} localpdf does not have expected path {}'.format(id_journalpaper, path_expected)
                )

    def test_journalpapers_id_format(self) -> None:
        """
        Confirm the journalpaper id is in the expected format.
        """
        for id_journalpaper, journalpaper in self.data['journalpapers'].items():
            id_journal = re.match('id_journal_(.*)', journalpaper['journal']).group(1)
            year = journalpaper['year']
            id_author = re.match('id_author_(.*)', journalpaper['authors'][0]).group(1).split('_')[0]

            id_expected = 'id_journalpaper_{}{}_{}'.format(
                id_journal,
                year,
                id_author
            )
            if 'slug' in journalpaper:
                id_expected += '_{}'.format(
                    journalpaper['slug']
                )

            self.assertEquals(
                id_journalpaper,
                id_expected,
                '{} does not have expected id {}'.format(id_journalpaper, id_expected)
            )

    def test_journalpapers_id_unique(self) -> None:
        """
        Confirm every journalpaper id is unique.

        The YAML parser does not error on this, and just keeps the most recently parsed.

        So we need to look at the file ourself.
        """
        with open('_data/journalpapers.yml') as f:
            id_existing = set()
            for line in f:
                match = re.match('(id_journalpaper_.*):', line)
                if match:
                    id_journalpaper = match.group(1)

                    self.assertNotIn(
                        id_journalpaper,
                        id_existing,
                        '{} is duplicated in journalpapers.yml'.format(id_journalpaper)
                    )

                    id_existing.add(id_journalpaper)

            self.assertGreater(
                len(id_existing),
                0,
                'No ID were parsed in journalpapers.yml'
            )
