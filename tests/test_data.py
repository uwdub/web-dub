import os.path
import unittest
import yaml


class TestData(unittest.TestCase):
    def setUp(self):
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

    def test_parse_yaml(self):
        pass

    def test_conferencepapers_authors_exist(self):
        for id_conferencepaper, conferencepaper in self.data['conferencepapers'].items():
            for id_author in conferencepaper['authors']:
                self.assertIn(
                    id_author,
                    self.data['authors'],
                    '{} not found in authors.yml'.format(id_author)
                )

    def test_conferencepapers_conference_exist(self):
        for id_conferencepaper, conferencepaper in self.data['conferencepapers'].items():
            id_conference = conferencepaper['conference']
            self.assertIn(
                id_conference,
                self.data['conferences'],
                '{} not found in conferences.yml'.format(id_conference)
            )

    def test_conferencepapers_files_exist(self):
        for id_conferencepaper, conferencepaper in self.data['conferencepapers'].items():
            # Every paper should have a thumb
            self.assertIn(
                'localthumb',
                conferencepaper,
                'localthumb not found in conferencepaper {}'.format(id_conferencepaper)
            )
            file_path = conferencepaper['localthumb']
            self.assertTrue(
                os.path.isfile('publications/{}'.format(file_path)),
                '{} not found in publications/'.format(file_path)
            )

            # Papers may have a PDF
            if 'localpdf' in conferencepaper:
                file_path = conferencepaper['localpdf']
                self.assertTrue(
                    os.path.isfile('publications/{}'.format(file_path)),
                    '{} not found in publications/'.format(file_path)
                )

            # Papers may have a video
            if 'localvideo' in conferencepaper:
                file_path = conferencepaper['localvideo']
                self.assertTrue(
                    os.path.isfile('publications/{}'.format(file_path)),
                    '{} not found in publications/'.format(file_path)
                )

    def test_journalpapers_authors_exist(self):
        for id_journalpaper, journalpaper in self.data['journalpapers'].items():
            for id_author in journalpaper['authors']:
                self.assertIn(
                    id_author,
                    self.data['authors'],
                    '{} not found in authors.yml'.format(id_author)
                )

    def test_journalpapers_journal_exist(self):
        for id_journalpaper, journalpaper in self.data['journalpapers'].items():
            id_journal = journalpaper['journal']
            self.assertIn(
                id_journal,
                self.data['journals'],
                '{} not found in journals.yml'.format(id_journal)
            )

    def test_journalpapers_files_exist(self):
        for id_journalpaper, journalpaper in self.data['journalpapers'].items():
            # Every paper should have a thumb
            self.assertIn(
                'localthumb',
                journalpaper,
                'localthumb not found in journalpaper {}'.format(id_journalpaper)
            )
            file_path = journalpaper['localthumb']
            self.assertTrue(
                os.path.isfile('publications/{}'.format(file_path)),
                '{} not found in publications/'.format(file_path)
            )

            # Papers may have a PDF
            if 'localpdf' in journalpaper:
                file_path = journalpaper['localpdf']
                self.assertTrue(
                    os.path.isfile('publications/{}'.format(file_path)),
                    '{} not found in publications/'.format(file_path)
                )

    def test_workshoppapers_authors_exist(self):
        for id_workshoppaper, workshoppaper in self.data['workshoppapers'].items():
            for id_author in workshoppaper['authors']:
                self.assertIn(
                    id_author,
                    self.data['authors'],
                    '{} not found in authors.yml'.format(id_author)
                )

    def test_workshoppapers_workshop_exist(self):
        for id_workshoppaper, workshoppaper in self.data['workshoppapers'].items():
            id_workshop = workshoppaper['workshop']
            self.assertIn(
                id_workshop,
                self.data['workshops'],
                '{} not found in workshops.yml'.format(id_workshop)
            )

    def test_workshoppapers_files_exist(self):
        for id_workshoppaper, workshoppaper in self.data['workshoppapers'].items():
            # Papers may have a PDF
            if 'localpdf' in workshoppaper:
                file_path = workshoppaper['localpdf']
                self.assertTrue(
                    os.path.isfile('publications/{}'.format(file_path)),
                    '{} not found in publications/'.format(file_path)
                )

