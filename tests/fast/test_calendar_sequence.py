import hashlib
import nose.tools
import os
import posixpath
import yaml


class TestSeminarSequence(object):
    def test_seminar_sequences_incremented(self):
        # Obtain our stored sequences
        with open('_compile-calendar-sequences.yml', encoding='utf-8') as f:
            seminar_calendar_sequences = yaml.safe_load(f)['sequences']

        # Iterate over all our seminar files
        seminar_paths = [
            os.path.normpath(seminar_file_entry.path)
            for seminar_file_entry
            in os.scandir('_seminars')
            if seminar_file_entry.is_file() and
               os.path.normpath(seminar_file_entry.path) != os.path.normpath('_seminars/_template.md') and
               os.path.normpath(seminar_file_entry.path) != os.path.normpath('_seminars/_template.j2')
        ]

        for seminar_path_current in seminar_paths:
            # Get the hash and sequence from the file
            with open(seminar_path_current, encoding='utf-8') as f:
                hash = hashlib.md5()
                for line in f:
                    hash.update(line.strip().encode(encoding='utf-8'))
                seminar_hash_current = hash.hexdigest()
            with open(seminar_path_current, encoding='utf-8') as f:
                seminar_sequence_current = list(yaml.safe_load_all(f))[0]['sequence']

            # Regardless of platform we're on, standardize the path we store (e.g., slashes)
            seminar_path_stored = posixpath.join(*os.path.normpath(seminar_path_current).split(os.sep))

            if seminar_path_stored not in seminar_calendar_sequences:
                seminar_calendar_sequences[seminar_path_stored] = {
                    'hash': seminar_hash_current,
                    'sequence': seminar_sequence_current
                }

            seminar_hash_stored = seminar_calendar_sequences[seminar_path_stored]['hash']
            seminar_sequence_stored = seminar_calendar_sequences[seminar_path_stored]['sequence']

            if seminar_hash_current != seminar_hash_stored:
                nose.tools.assert_greater(
                    seminar_sequence_current,
                    seminar_sequence_stored,
                    'Sequence was not incremented in {}'.format(seminar_path_current)
                )
