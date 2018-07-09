import os
import unittest
import yaml


class TestPeople(unittest.TestCase):
    def test_people_parse(self):
        """
        All people files parse as valid YAML.
        """
        extensions = {".jpg", ".png", ".gif"}  # etc

        people_paths = [
            people_file_entry.path
            for people_file_entry
            in os.scandir('_people')
            if (people_file_entry.is_file()) and (os.path.splitext(people_file_entry.path)[1] == ".md")
            ]
        for people_path_current in people_paths:
            try:
                with open(people_path_current) as f:
                    blocks = list(yaml.safe_load_all(f))
            except UnicodeDecodeError as e:
                self.assertIsNone(
                    e,
                    'Unicode error parsing people file: {}'.format(people_path_current)
                )

            self.assertIsNotNone(
                blocks,
                'Could not parse people file: {}'.format(people_path_current)
            )

    def test_people_fields(self):
        """
        All people files have valid contents.
        """
        people_paths = [
            people_file_entry.path
            for people_file_entry
            in os.scandir('_people')
            and os.scandir('_people/faculty')
            if people_file_entry.is_file()
            and not people_file_entry.path.endswith('README.md')
            and os.path.splitext(people_file_entry.path)[1] == ".md"
        ]

        for people_path_current in people_paths:
            with open(people_path_current) as f:
                # First block should be our header
                person = list(yaml.safe_load_all(f))[0]

            # It has a version with an allowable value
            self.assertIn(
                'version',
                person,
                'No version in {}'.format(people_path_current)
            )
            self.assertIn(
                str(person['version']),
                ['1'],
                'Invalid version in {}'.format(people_path_current)
            )

            # Role should exist
            self.assertIn(
                'role',
                person,
                'Missing role in {}'.format(people_path_current)
            )
            # Should be a valid role
            for role_current in person['role']:
                self.assertIn(
                    role_current,
                    [
                        'faculty',
                    ],
                    'Invalid role in {}'.format(people_path_current)
                )

            # Positions should exist
            self.assertIn(
                'positions',
                person,
                'Missing positions in {}'.format(people_path_current)
            )
            # Should be valid positions
            for position_current in person['positions']:
                if 'faculty' in person['role']:
                    # Faculty title should exist
                    self.assertIn(
                        'title',
                        position_current,
                        'Missing title in {}'.format(people_path_current)
                    )
                    # Faculty title should be valid
                    self.assertIn(
                        position_current['title'],
                        [
                            'Adjunct Assistant Professor',
                            'Adjunct Associate Professor',
                            'Adjunct Lecturer',
                            'Adjunct Senior Lecturer',
                            'Adjunct Professor',
                            'Affiliate Assistant Professor',
                            'Affiliate Associate Professor',
                            'Affiliate Professor',
                            'Assistant Professor',
                            'Associate Professor',
                            'Lecturer',
                            'Other <please email dub-web@dub.washington.edu>',
                            'Professor',
                            'Professor Emeritus',
                            'Senior Lecturer',
                        ],
                        'Invalid title in {}'.format(people_path_current)
                    )
                else:
                    # Non-faculty title should not exist
                    self.assertNotIn(
                        'title',
                        position_current,
                        'Title should not exist in {}'.format(people_path_current)
                    )

                # Affiliation should exist
                self.assertIn(
                    'affiliation',
                    position_current,
                    'Missing affiliation in {}'.format(people_path_current)
                )
                # Faculty affiliation should be valid
                self.assertIn(
                    position_current['affiliation'],
                    [
                        'Architecture',
                        'Biomedical Informatics and Medical Education',
                        'Civil & Environmental Engineering',
                        'Communication',
                        'Computer Science & Engineering',
                        'Division of Design',
                        'Electrical Engineering',
                        'Human Centered Design & Engineering',
                        'Human Computer Interaction + Design',
                        'Industrial & Systems Engineering',
                        'Information School',
                        'Mechanical Engineering',
                        'Other <please email dub-web@dub.washington.edu>',
                    ],
                    'Invalid affiliation in {}'.format(people_path_current)
                )

            # The website may be tbd
            if 'tbd_web' in person:
                # If the field exists, its value must be True
                self.assertTrue(
                    person['tbd_web'],
                    'Invalid tbd_web in {}'.format(people_path_current)
                )
                # Should be missing or have our template value
                if 'web' in person:
                    self.assertEqual(
                        person['web'],
                        None,
                        'Inconsistent tbd_web and web in {}'.format(people_path_current)
                    )
            else:
                # Website should exist
                self.assertIn(
                    'web',
                    person,
                    'Inconsistent tbd_web and web in {}'.format(people_path_current)
                )
                # Should not be our template value
                self.assertNotEqual(
                    person['web'],
                    None,
                    'Inconsistent tbd_web and web in {}'.format(people_path_current)
                )
