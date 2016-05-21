---
################################################################################
# Version of the seminar format. The only valid value for this is '1'. 
# We may increment this in the future to simplify maintenance of old seminars.
################################################################################
version: 1

################################################################################
# Sequence number of the seminar file. This is used to keep the iCal up to date.
# Increment the sequence number each time the seminar file is updated.
################################################################################
sequence: 0

################################################################################
# Date and time of the seminar. In quotes because : is a reserved character.
# Date must equal the name of this file.
################################################################################
date:     2015-10-07
time:     "12:00 PM"
time_end: "1:20 PM"

################################################################################
# A seminar file might exist but lack values for some fields. These are 'TBD'. 
# The only valid value is 'True'. A TBD field should not be present if 'False'.
################################################################################
tbd_speakers:   true
tbd_title:      true
tbd_location:   true
tbd_abstract:   true
tbd_bio:        true
tbd_video:      true

################################################################################
# Seminar files are archived by default.
# Add the following line if the file should not be archived:
#
# archive: false
################################################################################

################################################################################
# One or more speakers. Each speaker has name and affiliation.
#
# If a speaker does not have an affiliation, the affiliation field can be removed.
# In this case, the speaker needs a field 'affiliation_none: true'.
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
################################################################################
speakers:

################################################################################
# Our core fields are title, location, abstract, bio.
# title:      "Title in Quotes: Because Colons Cause Errors"
# 
# location:   "HUB 334"
# 
# abstract:   |
#   An abstract can span multiple lines, and can do things across those lines,
#   like going on for a while or being repetitive.
# 
# bio:        |
#   And do not even get us started on how a bio can be. Bio definitely can
#   also span multiple lines like this.
################################################################################
title:      "TBD"

location:   "TBD"

abstract:   |
  TBD
  
bio:        |
  TBD

################################################################################
# A seminar may have a video. If so, provide the Vimeo video number.
#
# video: 142303577
#
# If not, this field should not be present 
################################################################################
---
