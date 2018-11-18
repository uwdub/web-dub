import base.invoke.tasks.dependencies
from datetime import datetime
import hashlib
import icalendar
import invoke
import markdown
import os
import posixpath
import pytz
import re
import yaml


def _get_seminar_paths():
    seminar_paths = [
        os.path.normpath(seminar_file_entry.path)
        for seminar_file_entry
        in os.scandir('_seminars')
        if (
                seminar_file_entry.is_file()
                and os.path.splitext(seminar_file_entry.name)[1] == '.md'
                and seminar_file_entry.name != '_template.md'
        )
    ]

    return seminar_paths


@invoke.task(pre=[
    base.invoke.tasks.dependencies.dependencies_ensure
])
def compile_calendar():
    # Obtain our stored sequences
    with open('_compile-calendar-sequences.yml', encoding='utf-8') as f:
        seminar_calendar_sequences = yaml.safe_load(f)['sequences']
    # Iterate over all our seminar files
    seminar_paths = _get_seminar_paths()

    # Maintain the sequence field for each seminar
    for seminar_path_current in seminar_paths:
        # Get the hash and sequence from the file, to compare against our stored data
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
            # This is a seminar that is new to our sequence tracking,
            # decrement the initial sequence so it will be hashed and incremented
            seminar_calendar_sequences[seminar_path_stored] = {
                'hash': 'invalid_hash_to_force_update',
                'sequence': seminar_sequence_current - 1
            }

        seminar_hash_stored = seminar_calendar_sequences[seminar_path_stored]['hash']
        seminar_sequence_stored = seminar_calendar_sequences[seminar_path_stored]['sequence']
        if seminar_hash_current != seminar_hash_stored:
            # # Change detected, we need to bump the sequence
            # seminar_sequence_current = max(seminar_sequence_current, seminar_sequence_stored) + 1
            #
            # # pyyaml does not preserve comments, so we brute force modification of the seminar yml file
            # with open(seminar_path_current, encoding='utf-8') as f:
            #     seminar_contents = f.read()
            # seminar_contents = re.sub(
            #     'sequence: {}'.format('(\d*)'),
            #     'sequence: {}'.format(seminar_sequence_current),
            #     seminar_contents
            # )
            # with open(seminar_path_current, 'w', encoding='utf-8') as f:
            #     f.write(seminar_contents)
            #
            # # That changed the file, so update our hash, then store the updated sequence
            # with open(seminar_path_current, 'rb') as f:
            #     seminar_hash_current = hashlib.md5(f.read()).hexdigest()
            #
            # seminar_calendar_sequences[seminar_path_stored] = {
            #     'hash': seminar_hash_current,
            #     'sequence': seminar_sequence_current
            # }

            if seminar_sequence_current > seminar_sequence_stored:
                seminar_calendar_sequences[seminar_path_stored] = {
                    'hash': seminar_hash_current,
                    'sequence': seminar_sequence_current
                }

    # Store our updated sequences
    data = {'sequences': seminar_calendar_sequences}
    with open('_compile-calendar-sequences.yml', 'w', encoding='utf-8') as f:
        yaml.dump(
            data,
            stream=f,
            default_flow_style=False
        )

    # Now generate the ics file from our seminars and their sequences
    ics = icalendar.Calendar()
    ics.add('PRODID', '-//DUB//DUB Calendar')
    ics.add('VERSION', '2.0')
    ics.add('CALSCALE','GREGORIAN')
    ics.add('METHOD', 'PUBLISH')
    ics.add('X-WR-CALNAME', 'DUB Calendar')
    ics.add('X-WR-TIMEZONE', 'America/Los_Angeles')
    ics.add('X-WR-CALDESC', 'Calendar of DUB seminars.')

    for seminar_path_current in seminar_paths:
        # Parse the seminar
        with open(seminar_path_current, encoding='utf-8') as f:
            seminar_contents = list(yaml.safe_load_all(f))[0]

        # Add seminar as calendar event
        ics_event = icalendar.Event()

        # Give it a UID
        ics_event.add(
            'UID',
            seminar_contents['date'].strftime('%Y-%m-%d') + '@dub.washington.edu'
        )

        # Give it DTSTART and DTEND
        timezone = pytz.timezone('America/Los_Angeles')
        seminar_start_time = timezone.localize(datetime.combine(
            seminar_contents['date'],
            datetime.strptime(seminar_contents['time'], '%I:%M %p').time()
        ))
        seminar_end_time = timezone.localize(datetime.combine(
            seminar_contents['date'],
            datetime.strptime(seminar_contents['time_end'], '%I:%M %p').time()
        ))
        ics_event.add('DTSTART', seminar_start_time)
        ics_event.add('DTEND', seminar_end_time)

        # Generate SUMMARY from applicable components
        if seminar_contents.get('no_seminar', False):
            # Flagged as not having a seminar

            # Title should indicate why there's no seminar
            seminar_summary = seminar_contents['title']
        else:
            # We have a seminar, but its data may not yet be complete
            seminar_summary = 'DUB Seminar'

            if not seminar_contents.get('tbd_speakers', False):
                # We have speakers

                # If they all have the same affiliation, we'll collapse it, so let's check
                speaker_affiliations = [
                    speaker_current['affiliation'] if not speaker_current.get('affiliation_none', False) else 'affiliation_none'
                    for speaker_current
                    in seminar_contents['speakers']
                ]
                if len(set(speaker_affiliations)) == 1:
                    # Everybody has the same affiliation
                    # But it's still possible that affiliation is affiliation_none
                    if not seminar_contents['speakers'][0].get('affiliation_none', False):
                        # We have a legit affiliation
                        seminar_summary = '{} - {} ({})'.format(
                            seminar_summary,
                            ', '.join(
                                [
                                    ' '.join(speaker_current['name'][1:] + [speaker_current['name'][0]])
                                    for speaker_current
                                    in seminar_contents['speakers']
                                ]
                            ),
                            seminar_contents['speakers'][0]['affiliation']
                        )
                    else:
                        # Everybody has no affiliation
                        seminar_summary = '{} - {}'.format(
                            seminar_summary,
                            ', '.join(
                                [
                                    ' '.join(speaker_current['name'][1:] + [speaker_current['name'][0]])
                                    for speaker_current
                                    in seminar_contents['speakers']
                                ]
                            )
                        )
                else:
                    # Distinct affiliations
                    seminar_summary = '{} - {}'.format(
                        seminar_summary,
                        ', '.join(
                            [
                                '{}{}'.format(
                                    ' '.join(speaker_current['name'][1:] + [speaker_current['name'][0]]),
                                    '({})'.format(speaker_current['affiliation']) if not speaker_current.get('affiliation_none', False) else ''
                                )
                                for speaker_current
                                in seminar_contents['speakers']
                            ]
                        )
                    )

            if not seminar_contents.get('tbd_title', False):
                # We have a title
                seminar_summary = '{} - "{}"'.format(
                    seminar_summary,
                    seminar_contents['title']
                )

        ics_event.add('SUMMARY', seminar_summary)

        # Add the location unless it has an override
        if not seminar_contents.get('no_seminar', False):
            if seminar_contents.get('location_override_calendar', False):
                ics_event.add('LOCATION', seminar_contents['location_override_calendar'])
            else:
                ics_event.add('LOCATION', seminar_contents['location'])

        # This description generation is still a bit sketchy, should decide what we want
        #
        # Generate description string from applicable components
        if not seminar_contents.get('no_seminar', False):
            description_string = ''
            if 'text_override_seminar_page' in seminar_contents:
                description_string = seminar_contents['text_override_seminar_page']
            else:
                if 'tbd_bio' not in seminar_contents:
                    if 'tbd_abstract' not in seminar_contents:
                        description_string = seminar_contents['abstract'] + '\r\n' + seminar_contents['bio']
                    else:
                        description_string = seminar_contents['bio']
                elif 'tbd_abstract' not in seminar_contents:
                    description_string = seminar_contents['abstract']

            # This was crashing, and I couldn't easily determine why, so I've temporarily removed it
            #
            # # Parse description as markdown
            # class SensibleParagraphs(markdown.extensions.Extension):
            #     def extendMarkdown(self, md, md_globals):
            #         br_tag = markdown.inlinepatterns.SubstituteTagPattern(r'\n', None)
            #         md.inlinePatterns.add('nl', br_tag, '_end')
            #
            # ics_event.add('DESCRIPTION', markdown.markdown(description_string, extensions=[SensibleParagraphs()]))

        # That's our complete event
        ics.add_component(ics_event)

    # Store the ics file output
    with open('calendar.ics', 'wb') as f:
        f.write(ics.to_ical())


@invoke.task(pre=[
    base.invoke.tasks.dependencies.dependencies_ensure
])
def compile_calendar_increment_all_sequences():
    # Obtain our stored sequences
    with open('_compile-calendar-sequences.yml', encoding='utf-8') as f:
        seminar_calendar_sequences = yaml.safe_load(f)['sequences']

    # Iterate over all our seminar files
    seminar_paths = _get_seminar_paths()

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

        # Bump the sequence
        seminar_sequence_current = max(seminar_sequence_current, seminar_sequence_stored) + 1

        # pyyaml does not preserve comments, so we brute force modification of the seminar yml file
        with open(seminar_path_current, encoding='utf-8') as f:
            seminar_contents = f.read()
        seminar_contents = re.sub(
            'sequence: {}'.format('(\d*)'),
            'sequence: {}'.format(seminar_sequence_current),
            seminar_contents
        )
        with open(seminar_path_current, 'w', encoding='utf-8') as f:
            f.write(seminar_contents)

        # That changed the file, so update our hash, then store the updated sequence
        with open(seminar_path_current, encoding='utf-8') as f:
            hash = hashlib.md5()
            for line in f:
                hash.update(line.strip().encode(encoding='utf-8'))
            seminar_hash_current = hash.hexdigest()

        seminar_calendar_sequences[seminar_path_stored] = {
            'hash': seminar_hash_current,
            'sequence': seminar_sequence_current
        }

    # Store our updated sequences
    data = {'sequences': seminar_calendar_sequences}
    with open('_compile-calendar-sequences.yml', 'w', encoding='utf-8') as f:
        yaml.dump(
            data,
            stream=f,
            default_flow_style=False
        )
