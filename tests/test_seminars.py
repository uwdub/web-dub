import os
import unittest
import yaml


class TestSeminars(unittest.TestCase):
    def test_seminars_parse(self):
        """
        All seminar files parse as valid YAML.
        """
        seminar_paths = [
            seminar_file_entry.path
            for seminar_file_entry
            in os.scandir('_seminars')
            if seminar_file_entry.is_file()
        ]
        for seminar_path_current in seminar_paths:
            try:
                with open(seminar_path_current) as f:
                    blocks = list(yaml.safe_load_all(f))
            except UnicodeDecodeError as e:
                self.assertIsNone(
                    e,
                    'Unicode error parsing seminar file: {}'.format(seminar_path_current)
                )

            self.assertIsNotNone(
                blocks,
                'Could not parse seminar file: {}'.format(seminar_path_current)
            )

    def test_seminars_fields(self):
        """
        All seminar files have valid contents.
        """
        seminar_paths = [
            seminar_file_entry.path
            for seminar_file_entry
            in os.scandir('_seminars')
            if seminar_file_entry.is_file()
        ]
        for seminar_path_current in seminar_paths:
            with open(seminar_path_current) as f:
                # First block should be our header
                seminar = list(yaml.safe_load_all(f))[0]

            # It has a version with an allowable value
            self.assertIn(
                'version',
                seminar,
                'No version in {}'.format(seminar_path_current)
            )
            self.assertIn(
                str(seminar['version']),
                ['1'],
                'Invalid version in {}'.format(seminar_path_current)
            )

            # The sequence is not 0, unless we're looking at the _template.md
            self.assertIn(
                'sequence',
                seminar,
                'No sequence in {}'.format(seminar_path_current)
            )
            if os.path.normpath(seminar_path_current) != os.path.normpath('_seminars/_template.md'):
                self.assertGreater(
                    seminar['sequence'],
                    0,
                    'Sequence was not incremented in {}'.format(seminar_path_current)
                )

            # It has date and time fields
            self.assertIn(
                'date',
                seminar,
                'No date in {}'.format(seminar_path_current)
            )
            self.assertIn(
                'time',
                seminar,
                'No time in {}'.format(seminar_path_current)
            )
            self.assertIn(
                'time_end',
                seminar,
                'No time_end in {}'.format(seminar_path_current)
            )

            # The date matches the filename, unless we're looking at the _template.md
            if os.path.normpath(seminar_path_current) != os.path.normpath('_seminars/_template.md'):
                self.assertEquals(
                    os.path.normpath('_seminars/{}.md'.format(seminar['date'])),
                    os.path.normpath(seminar_path_current),
                    'Date does not match filename in {}'.format(seminar_path_current)
                )

            # The speaker may be tbd
            if 'tbd_speakers' in seminar:
                # If the field exists, its value must be True
                self.assertTrue(
                    seminar['tbd_speakers'],
                    'Invalid tbd_speakers in {}'.format(seminar_path_current)
                )
                # Should be missing or have our template value
                if 'speakers' in seminar:
                    self.assertEqual(
                        seminar['speakers'],
                        None,
                        'Inconsistent tbd_speakers and speakers in {}'.format(seminar_path_current)
                    )
            else:
                # Speakers should exist
                self.assertIn(
                    'speakers',
                    seminar,
                    'Inconsistent tbd_speakers and speakers in {}'.format(seminar_path_current)
                )
                # Should not be our template value
                self.assertNotEqual(
                    seminar['speakers'],
                    None,
                    'Inconsistent tbd_speakers and speakers in {}'.format(seminar_path_current)
                )
                # One or more speakers, each of which has a name and affiliation
                for speaker_current in seminar['speakers']:
                    self.assertIn(
                        'name',
                        speaker_current,
                        'Missing speakers name in {}'.format(seminar_path_current)
                    )
                    if 'affiliation_none' in speaker_current:
                        self.assertEqual(
                            speaker_current['affiliation_none'],
                            True,
                            'Inconsistent value for speakers affiliation_none in {}'.format(seminar_path_current)
                        )
                    else:
                        self.assertIn(
                            'affiliation',
                            speaker_current,
                            'Missing speakers affiliation in {}'.format(seminar_path_current)
                        )

            # The title may be tbd
            if 'tbd_title' in seminar:
                # If the field exists, its value must be True
                self.assertTrue(
                    seminar['tbd_title'],
                    'Invalid tbd_title in {}'.format(seminar_path_current)
                )
                # Should be missing or have our template value
                if 'title' in seminar:
                    self.assertEqual(
                        seminar['title'],
                        'TBD',
                        'Inconsistent tbd_title and title in {}'.format(seminar_path_current)
                    )
            else:
                # Title should exist
                self.assertIn(
                    'title',
                    seminar,
                    'Inconsistent tbd_title and title in {}'.format(seminar_path_current)
                )
                # Should not be our template value
                self.assertNotEqual(
                    seminar['title'],
                    'TBD',
                    'Inconsistent tbd_title and title in {}'.format(seminar_path_current)
                )

            # The location may be tbd
            if 'tbd_location' in seminar:
                # If the field exists, its value must be True
                self.assertTrue(
                    seminar['tbd_location'],
                    'Invalid tbd_location in {}'.format(seminar_path_current)
                )
                # Should be missing or have our template value
                if 'location' in seminar:
                    self.assertEqual(
                        seminar['location'],
                        'TBD',
                        'Inconsistent tbd_location and location in {}'.format(seminar_path_current)
                    )
            else:
                # Location should exist
                self.assertIn(
                    'location',
                    seminar,
                    'Inconsistent tbd_location and location in {}'.format(seminar_path_current)
                )
                # Should not be our template value
                self.assertNotEqual(
                    seminar['location'],
                    'TBD',
                    'Inconsistent tbd_location and location in {}'.format(seminar_path_current)
                )
                # Should be a valid location
                self.assertIn(
                    seminar['location'],
                    [
                        'Alder Commons',
                        'CSE 691',
                        'Haggett Hall Cascade Room',
                        'HUB 145',
                        'HUB 250',
                        'HUB 332',
                        'HUB 334',
                        'Sieg 233',
                        'StartUp Hall Meeting Room, 1100 NE Campus Parkway'
                    ],
                    'Invalid location in {}'.format(seminar_path_current)
                )

            # The abstract may be tbd
            if 'tbd_abstract' in seminar:
                # If the field exists, its value must be True
                self.assertTrue(
                    seminar['tbd_abstract'],
                    'Invalid tbd_abstract in {}'.format(seminar_path_current)
                )
                # Should be missing or have our template value
                if 'abstract' in seminar:
                    self.assertEqual(
                        seminar['abstract'],
                        'TBD\n',
                        'Inconsistent tbd_abstract and abstract in {}'.format(seminar_path_current)
                    )
            else:
                # Abstract should exist
                self.assertIn(
                    'abstract',
                    seminar,
                    'Inconsistent tbd_abstract and abstract in {}'.format(seminar_path_current)
                )
                # Should not be our template value
                self.assertNotEqual(
                    seminar['abstract'],
                    'TBD\n',
                    'Inconsistent tbd_abstract and abstract in {}'.format(seminar_path_current)
                )

            # The bio may be tbd
            if 'tbd_bio' in seminar:
                # If the field exists, its value must be True
                self.assertTrue(
                    seminar['tbd_bio'],
                    'Invalid tbd_bio in {}'.format(seminar_path_current)
                )
                # Should be missing or have our template value
                if 'bio' in seminar:
                    self.assertEqual(
                        seminar['bio'],
                        'TBD\n',
                        'Inconsistent tbd_bio and bio in {}'.format(seminar_path_current)
                    )
            else:
                # Bio should exist
                self.assertIn(
                    'bio',
                    seminar,
                    'Inconsistent tbd_bio and bio in {}'.format(seminar_path_current)
                )
                # Should not be our template value
                self.assertNotEqual(
                    seminar['bio'],
                    'TBD\n',
                    'Inconsistent tbd_bio and bio in {}'.format(seminar_path_current)
                )

            # The video may be tbd
            if 'tbd_video' in seminar:
                # If the field exists, its value must be True
                self.assertTrue(
                    seminar['tbd_video'],
                    'Invalid tbd_video in {}'.format(seminar_path_current)
                )
                # Should be missing or have our template value
                self.assertNotIn(
                    'video',
                    seminar,
                    'Invalid video in {}'.format(seminar_path_current)
                )
            else:
                # Video should exist
                self.assertIn(
                    'video',
                    seminar,
                    'Inconsistent tbd_video and video in {}'.format(seminar_path_current)
                )
                # It should be an integer
                self.assertEqual(
                    type(seminar['video']),
                    int,
                    'Invalid video in {}'.format(seminar_path_current)
                )
