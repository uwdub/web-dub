import os
import unittest
import yaml


class TestPeople(unittest.TestCase):
    def test_people_parse(self):
        """
        All people files parse as valid YAML.
        """
        extensions = {".jpg", ".png", ".gif"} #etc

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
            in os.scandir('_people') and
                os.scandir('_people/faculty') and
                os.scandir('_people/doctoral/_unchecked') and
                os.scandir('_people/masters/_unchecked')
            if (people_file_entry.is_file()) and (os.path.splitext(people_file_entry.path)[1] == ".md")
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
                        'doctoral',
                        'masters',
                        'undergrad',
                        'industry',
                        'alumni-faculty',
                        'alumni-doctoral',
                        'alumni-masters',
                        'alumni-undergrad'
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
                            'Assistant Professor',
                            'Associate Professor',
                            'Professor',
                            'Professor Emeritus',
                            'Lecturer',
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
                # Affiliation should be valid
                if 'masters' in person['role']:
                    # Masters affiliation should be valid
                    self.assertIn(
                        position_current['affiliation'],
                        [
                            'Master of Science in Computer Science & Engineering',
                            'Master of Design',
                            'Master of Science in Human Centered Design & Engineering',
                            'Master of Science in Information Management',
                            'Master of Library and Information Science',
                            'Master of Human-Computer Interaction + Design',
                            'Master of Science in Architecture',
                            'Master of Science in Biomedical & Health Informatics',
                            'Master of Communication in Digital Media',
                            'Master of Communication in Communities and Networks',
                            'Master of Science in Electrical Engineering',
                            'Master of Industrial & Systems Engineering',
                            'Master of Science in Industrial Engineering',
                            'Master of Science in Mechanical Engineering',
                            'Master of Science in Engineering'
                        ],
                        'Invalid affiliation in {}'.format(people_path_current)
                    )
                else:
                    # Faculty/doctoral affiliation should be valid
                    self.assertIn(
                        position_current['affiliation'],
                        [
                            'Computer Science & Engineering',
                            'Division of Design',
                            'Human Centered Design & Engineering',
                            'Information School',
                            'Human Computer Interaction & Design',
                            'Architecture',
                            'Biomedical & Health Informatics',
                            'Communication',
                            'DXARTS Digital Arts',
                            'Electrical Engineering',
                            'Industrial & Systems Engineering',
                            'Mechanical Engineering',
                            'Psychology',
                            'Civil & Environmental Engineering',
                            'Nursing',
                            'Rehabilitation Medicine',
                            'Interdisciplinary Arts & Sciences of UW Tacoma'
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
