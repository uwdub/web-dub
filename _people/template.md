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

################################################################################
# Full name listed in the order of last name, first name, middle name(s).
#
# name: 
#   - Surname
#   - First
#   - Middle
#   - More
################################################################################
name:
    - template

################################################################################
# Each person has a single role, which is out highest level grouping.
# A person may have multiple positions. Position consists of titles and units.
# Each value for a field must match one of the options below exactly.
#
# Valid roles: faculty, doctoral, masters, undergrad, staff
# Valid faculty titles: Associate Professor, Assistant Professor, Emeritus
# Valid faculty and doctoral units:
#   Computer Science & Engineering
#   Human Centered Design & Engineering
#   Human Computer Interaction & Design
#   Division of Design
#   Information School
# Valid masters units:
#   Master of Science  in Information Management
#   Master of Human-Computer Interaction + Design
#   Master of Science in Human Centered Design & Engineering
#
# Faculty have one or more title and units.
# role:
#  - faculty
# position:
#  - title: Associate Professor
#    unit: Information School
#  - title: Adjunct Associate Professor
#    unit: Computer Science & Engineering
# 
# Students do not have a title, but can have one more units.
#
# For a doctoral student their unit is the name of their department.
# role:
#  - doctoral-student
# position:
#  - unit: Information School
#
# For a master's student their unit is the name of their program.
#  role:
#  - masters-student
#  position:
#  - unit: Master of Science in Human Centered Design & Engineering
#
# 
################################################################################
role:
  - template role

position:
  - unit: template unit

################################################################################
# A person may have a website or twitter tag
#
# web:
# - http://faculty.washington.edu/ajko/
# twitter:
# - andyjko
################################################################################
web:

---
