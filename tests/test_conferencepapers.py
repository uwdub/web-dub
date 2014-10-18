import os.path
import re
import unittest
import yaml


class TestConferencePapers(unittest.TestCase):
    def setUp(self) -> None:
        """
        Parse our data files and combine them into a dictionary.
        """
        data_files = [
            'authors',
            'conferencepapers',
            'conferences'
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

    def test_conferences_id_format(self) -> None:
        """
        Confirm the conference id is in the expected format.
        """
        for id_conference, conference in self.data['conferences'].items():
            if id_conference in ('aliases_longname'):
                continue

            if 'id_override' in conference:
                id_expected = 'id_conference_{}'.format(
                    conference['id_override']
                )
            else:
                id_expected = 'id_conference_{}'.format(
                    conference['shortname'].lower().replace(' ', '').replace('.', '').replace('/', '')
                )

            self.assertEquals(
                id_conference,
                id_expected,
                '{} does not have expected id {}'.format(id_conference, id_expected)
            )

    def test_conferences_id_unique(self) -> None:
        """
        Confirm every conference id is unique.

        The YAML parser does not error on this, and just keeps the most recently parsed.

        So we need to look at the file ourself.
        """
        with open('_data/conferences.yml') as f:
            id_existing = set()
            for line in f:
                match = re.match('(id_conference_.*):', line)
                if match:
                    id_conference = match.group(1)

                    self.assertNotIn(
                        id_conference,
                        id_existing,
                        '{} is duplicated in conferences.yml'.format(id_conference)
                    )

                    id_existing.add(id_conference)

            self.assertGreater(
                len(id_existing),
                0,
                'No ID were parsed in conferences.yml'
            )

    def test_conferencepapers_authors_exist(self) -> None:
        """
        Confirm all authors referenced by a paper actually exist.
        """
        for id_conferencepaper, conferencepaper in self.data['conferencepapers'].items():
            for id_author in conferencepaper['authors']:
                self.assertIn(
                    id_author,
                    self.data['authors'],
                    '{} references author {} not found in authors.yml'.format(id_conferencepaper, id_author)
                )

    def test_conferencepapers_conference_exist(self) -> None:
        """
        Confirm all conferences referenced by a paper actually exist.
        """
        for id_conferencepaper, conferencepaper in self.data['conferencepapers'].items():
            id_conference = conferencepaper['conference']
            self.assertIn(
                id_conference,
                self.data['conferences'],
                '{} references conference {} not found in conferences.yml'.format(id_conferencepaper, id_conference)
            )

    def test_conferencepapers_files_exist(self) -> None:
        """
        Confirm all files references by a paper actually exist.
        """
        for id_conferencepaper, conferencepaper in self.data['conferencepapers'].items():
            # Every paper must have a thumb
            self.assertIn(
                'localthumb',
                conferencepaper,
                '{} missing field localthumb'.format(id_conferencepaper)
            )
            file_path = conferencepaper['localthumb']
            self.assertTrue(
                os.path.isfile('publications/{}'.format(file_path)),
                '{} references localthumb {} not found in publications/'.format(id_conferencepaper, file_path)
            )

            # Papers may have a PDF
            if 'localpdf' in conferencepaper:
                file_path = conferencepaper['localpdf']
                self.assertTrue(
                    os.path.isfile('publications/{}'.format(file_path)),
                    '{} references localpdf {} not found in publications/'.format(id_conferencepaper, file_path)
                )

            # Papers may have a video
            if 'localvideo' in conferencepaper:
                file_path = conferencepaper['localvideo']
                self.assertTrue(
                    os.path.isfile('publications/{}'.format(file_path)),
                    '{} references localvideo {} not found in publications/'.format(id_conferencepaper, file_path)
                )

    def test_conferencepapers_id_unique(self) -> None:
        """
        Confirm every conferencepaper id is unique.

        The YAML parser does not error on this, and just keeps the most recently parsed.

        So we need to look at the file ourself.
        """
        with open('_data/conferencepapers.yml') as f:
            id_existing = set()
            for line in f:
                match = re.match('(id_conferencepaper_.*):', line)
                if match:
                    id_conferencepaper = match.group(1)

                    self.assertNotIn(
                        id_conferencepaper,
                        id_existing,
                        '{} is duplicated in conferencepapers.yml'.format(id_conferencepaper)
                    )

                    id_existing.add(id_conferencepaper)

            self.assertGreater(
                len(id_existing),
                0,
                'No ID were parsed in conferencepapers.yml'
            )

