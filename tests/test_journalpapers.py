import os.path
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

    
    # def test_journals_format(self) -> None:
    #     '''
    #     Confirm journals format follows: id_conference_{}_{}.
    #     '''
    #     for id_journal, journal in self.data['journals'].items():
    #         split = id_journal.split('_')
    #         if 'id' in id_journal:
    #             self.assertGreater(len(split[2]),5)
    

    def test_journalpapers_id_unique(self) -> None:
        '''
        confirm every journalpapers has an unique id
        '''
        with open('_data/journalpapers.yml') as f:
            idset  = set()
            for line in f:
                if 'id_journalpaper' in line:
                    self.assertFalse(line in idset)
                    idset.add(line)


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
