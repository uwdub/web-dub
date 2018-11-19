---
################################################################################
# Version of the seminar file format.
#
# - The only valid value for this is '1'.
# - We may increment this in the future to simplify maintenance of old seminars.
################################################################################
version: 1

################################################################################
# Sequence number of the seminar file.
#
# - This is used to keep the iCal up to date.
# - Increment the sequence each time the seminar file is updated.
################################################################################
sequence: {{ sequence }}

################################################################################
# Date and time of the seminar.
#
# - Date must equal the name of this file.
# - Times must be in quotes because : is a reserved character.
################################################################################
date:     "{{ date }}"
time:     "{{ time }}"
time_end: "{{ time_end }}"

################################################################################
# A TBD field indicates some other field still lacks a meaningful value.
#
# - The only valid value is 'true'.
# - A field should not be present if 'false'.
################################################################################
{% if tbd_speakers is defined %}
tbd_speakers:   {{ tbd_speakers }}
{% endif %}
{% if tbd_title is defined %}
tbd_title:      {{ tbd_title }}
{% endif %}
{% if tbd_location is defined %}
tbd_location:   {{ tbd_location }}
{% endif %}
{% if tbd_abstract is defined %}
tbd_abstract:   {{ tbd_abstract }}
{% endif %}
{% if tbd_bio is defined %}
tbd_bio:        {{ tbd_bio }}
{% endif %}
{% if tbd_video is defined %}
tbd_video:      {{ tbd_video }}
{% endif %}

################################################################################
# If a date is "No DUB Seminar", it will be displayed differently.
#
# - The only valid value is 'True'.
# - A field should not be present if 'False'.
#
# no_seminar: true
################################################################################
{% if no_seminar is defined %}
no_seminar: {{ no_seminar }}
{% endif %}

################################################################################
# Seminar files are archived by default. Add this if a seminar should not be.
#
# - The only valid value is 'True'.
# - A field should not be present if 'False'.
#
# no_archive: true
################################################################################
{% if no_archive is defined %}
no_archive: {{ no_archive }}
{% endif %}

################################################################################
# One or more speakers. Each speaker has a name and affiliation.
#
# - Our style guide is that:
#   - UW affilitations are a program
#   - Non-UW academic affiliations are a university
#   - Non-UW corportate affiliations may include research (e.g., "Microsoft Research")
# - If a speaker does not have an affiliation:
#   - remove the affiliation field
#   - add a field 'affiliation_none: true'.
#
#
# speakers:
#   - name: 
#     - Surname
#     - First
#     - Middle
#     - More
#     affiliation: Computer Science & Engineering 
#   - name: 
#     - Surname
#     - First
#     - Middle
#     - More
#     affiliation: Information School 
#   - name: 
#     - Surname
#     - First
#     - Middle
#     - More
#     affiliation: Carnegie Mellon University 
#   - name:
#     - Surname
#     - First
#     - Middle
#     - More
#     affiliation_none: true
################################################################################
speakers:
{% if speakers is defined and speakers is iterable %}
  {% for speaker in speakers %}
  - name:
    {% for item_name in speaker.name %}
    - "{{ item_name }}"
    {% endfor %}
    {% if speaker.affiliation is defined %}
    affiliation: "{{ speaker.affiliation }}"
    {% endif %}
    {% if speaker.affiliation_none is defined %}
    affiliation_none: "{{ speaker.affiliation_none }}"
    {% endif %}
  {% endfor %}
{% endif %}

################################################################################
# Our core fields are title, location, abstract, bio.
#
# - title should be in quotes
#
# - location must be from a set of values:
#     "Alder Commons"
#     "CSE 691"
#     "GIX"
#     "Haggett Hall Cascade Room"
#     "HUB 145"
#     "HUB 250"
#     "HUB 332"
#     "HUB 334"
#     "HUB 340"
#     "Kane 220"
#     "Kane 225"
#     "More 230"
#     "Sieg 233"
#     "StartUp Hall Meeting Room"
#
# - if custom text is required for the title
#   - title_override_seminar_page:
#
# - if custom text is required for location
#   - location_override_calendar:
#   - location_override_seminar_page:
#
# - if the default layout is to be completely overridden
#   - text_override_seminar_page:
#
#
# title:      "Title in Quotes: Because Colons Cause Errors"
# location:   "HUB 334"
#
# abstract:   |
#   The | means that text actually starts on this line. Additional lines without
#   a blank between them are considered part of the same paragraph.
#
#   A blank line is then a new paragraph.
#
#   All lines must be indented two spaces, like in these paragraphs.
#
# bio:        |
#   Follows the same formatting as abstract.
#
#   All lines must be indented two spaces, like in these paragraphs.
################################################################################
title:      "{{ title | trim | replace("\"", "\\\"") }}"

{% if title_override_seminar_page is defined %}
title_override_seminar_page: |
  {{ title_override_seminar_page | indent(width=2)}}

{% endif %}
location:   "{{ location }}"

{% if location_override_calendar is defined %}
location_override_calendar: |
  {{ location_override_calendar | indent(width=2)}}

{% endif %}
{% if location_override_seminar_page is defined %}
location_override_seminar_page: |
  {{ location_override_seminar_page | indent(width=2)}}

{% endif %}
{% if abstract is defined %}
abstract: |
  {{ abstract | indent(width=2)}}

{% endif %}
{% if bio is defined %}
bio: |
  {{ bio | indent(width=2)}}

{% endif %}
{% if text_override_seminar_page is defined %}
text_override_seminar_page: |
  {{ text_override_seminar_page | indent(width=2)}}

{% endif %}
################################################################################
# A seminar may have a video.
#
# - If a seminar has a video, provide the Vimeo video number.
# - If there is no video, this field should not be present
#
# video: 142303577
################################################################################
{% if video is defined %}
video: {{ video }}
{% endif %}
---

