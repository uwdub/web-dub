# import os
# import unittest
# import yaml
#
#
# class TestSeminars(unittest.TestCase):
#     def test_seminars_parse(self):
#         """
#         All seminar files parse as valid YAML.
#         """
#         seminar_paths = [
#             seminar_file_entry.path
#             for seminar_file_entry
#             in os.scandir('_seminars')
#             if seminar_file_entry.is_file()
#         ]
#         for seminar_path_current in seminar_paths:
#             with open(seminar_path_current) as f:
#                 blocks = yaml.safe_load_all(f)
#
#             self.assertIsNotNone(
#                 blocks,
#                 'Could not parse seminar file: {}'.format(seminar_path_current)
#             )
#
#     def test_seminars_fields(self):
#         """
#         All seminar files have valid contents.
#         """
#         seminar_paths = [
#             seminar_file_entry.path
#             for seminar_file_entry
#             in os.scandir('_seminars')
#             if seminar_file_entry.is_file()
#         ]
#         for seminar_path_current in seminar_paths:
#             with open(seminar_path_current) as f:
#                 # First block should be our header
#                 seminar = list(yaml.safe_load_all(f))[0]
#
#             # It has a version with an allowable value
#             self.assertIn(
#                 'version',
#                 seminar,
#                 'No version in {}'.format(seminar_path_current)
#             )
#             self.assertIn(
#                 str(seminar['version']),
#                 ['1'],
#                 'Invalid version in {}'.format(seminar_path_current)
#             )
#
#             # It has date and time fields
#             self.assertIn(
#                 'date',
#                 seminar,
#                 'No date in {}'.format(seminar_path_current)
#             )
#             self.assertIn(
#                 'time',
#                 seminar,
#                 'No time in {}'.format(seminar_path_current)
#             )
#             self.assertIn(
#                 'time_end',
#                 seminar,
#                 'No time_end in {}'.format(seminar_path_current)
#             )
#
#             # The date matches the filename, unless we're looking at the _template.md
#             if os.path.normpath(seminar_path_current) != os.path.normpath('_seminars/_template.md'):
#                 self.assertEquals(
#                     os.path.normpath('_seminars/{}.md'.format(seminar['date'])),
#                     os.path.normpath(seminar_path_current),
#                     'Date does not match filename in {}'.format(seminar_path_current)
#                 )
#
#             # It might be tbd
#             if 'tbd' in seminar:
#                 # If the field exists, its value must be True
#                 self.assertTrue(
#                     seminar['tbd'],
#                     'Invalid tbd in {}'.format(seminar_path_current)
#                 )
#             else:
#                 # It might have one or more speakers, each of which has a name and affiliation
#                 if 'speakers' in seminar:
#                     for speaker_current in seminar['speakers']:
#                         self.assertIn(
#                             'name',
#                             speaker_current,
#                             'No name in {}'.format(seminar_path_current)
#                         )
#                         self.assertIn(
#                             'affiliation',
#                             speaker_current,
#                             'No affiliation in {}'.format(seminar_path_current)
#                         )
#
#                 # It has a title
#                 self.assertIn(
#                     'title',
#                     seminar,
#                     'No title in {}'.format(seminar_path_current)
#                 )
#
#                 # It has a valid location
#                 self.assertIn(
#                     'location',
#                     seminar,
#                     'No location in {}'.format(seminar_path_current)
#                 )
#                 self.assertIn(
#                     seminar['location'],
#                     ['TBD', 'CSE 691', 'HUB 145', 'HUB 250', 'HUB 332', 'HUB 334'],
#                     'Invalid location in {}'.format(seminar_path_current)
#                 )
#
#                 # It has an abstract
#                 self.assertIn(
#                     'abstract',
#                     seminar,
#                     'No abstract in {}'.format(seminar_path_current)
#                 )
#
#                 # It has a bio
#                 self.assertIn(
#                     'bio',
#                     seminar,
#                     'No bio in {}'.format(seminar_path_current)
#                 )
#
#                 # It might have a video field
#                 if 'video' in seminar:
#                     self.assertEqual(
#                         type(seminar['video']),
#                         int,
#                         'Invalid video in {}'.format(seminar_path_current)
#                     )
