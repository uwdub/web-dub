import os.path
import unittest
import yaml


class TestPubnum(unittest.TestCase):
    def setUp(self):
        data_files = [
            'conferencepapers',
            'journalpapers',
            'workshoppapers',
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

    def test_pubnums_removed(self) -> None:
        """
        Confirm none of our papers have a pubnum field.
        Such a field would be left over from importing from a personal site, and not meaningful here.
        """
        for id_conferencepaper, conferencepaper in self.data['conferencepapers'].items():
            self.assertNotIn('pubnum',conferencepaper)
        for id_journalpaper, journalpaper in self.data['journalpapers'].items():
            self.assertNotIn('pubnum',journalpaper)
        for id_workshoppaper, workshoppaper in self.data['workshoppapers'].items():
            self.assertNotIn('pubnum',workshoppaper)

