---
################################################################################
# Version of the people format. The only valid value for this is 1. 
# We may increment this in the future to simplify maintenance of old people.
################################################################################
version: 1

################################################################################
# A people file might exist but lack values for some fields. These are 'TBD'. 
# The only valid value is 'True'. A TBD field should not be present if 'False'.
################################################################################
tbd_web: true

################################################################################
# Full name listed in the order of last name, first name, middle name(s).
#
# name: 
# - Surname
# - First
# - Middle
# - More
################################################################################
name:
- Surname
- First
- Middle

################################################################################
# Each person has a single main role.
#
# Valid roles: faculty
################################################################################
role:
- faculty

################################################################################
# A person may have multiple positions, which consist of titles and affiliations.
#
# Faculty have one or more title and affiliations.
#
# Valid faculty titles: 
#   Assistant Professor 
#   Associate Professor 
#   Professor
#
#   Lecturer
#   Senior Lecturer
#
#   Professor Emeritus 
#
# Valid faculty and doctoral affiliations:
#   Computer Science & Engineering
#   Division of Design
#   Human Centered Design & Engineering
#   Information School
#
#   Human Computer Interaction & Design
#
#   Architecture
#   Biomedical & Health Informatics
#   Civil & Environmental Engineering
#   Communication
#   DXARTS Digital Arts
#   Electrical Engineering
#   Industrial & Systems Engineering
#   Mechanical Engineering
#   Nursing
#   Psychology
#   Rehabilitation Medicine
################################################################################
positions:
- title: Associate Professor
  affiliation: Computer Science & Engineering

################################################################################
# A person may have a website. If not, this field should not be present.
#
# web:
# - https://homes.cs.washington.edu/~jfogarty/
################################################################################

---
