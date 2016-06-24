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
# Each person has a single main role, and may have additional alumni roles.
# The first role that is listed is their main (current) role.
#
# Valid roles: faculty, doctoral, masters, undergrad, industry,
#              alumni-faculty, alumni-doctoral, alumni-masters, alumni-undergrad
################################################################################
role:
- faculty

################################################################################
# A person may have multiple positions, which consist of titles and affiliations.
#
# Faculty have one or more title and affiliations.
# Students do not have a title, but have one or more affiliations.
#
# For a doctoral student their affiliation is the name of their department.
# For a master's student their affiliation is the name of their program.
#
# Valid faculty titles: Assistant Professor, Associate Professor, Professor,
#                       Professor Emeritus, Lecturer, Senior Lecturer
#
# Valid faculty and doctoral affiliations:
#   Computer Science & Engineering
#   Human Centered Design & Engineering
#   Human Computer Interaction & Design
#   Information School
#   Division of Design
#   DXARTS Digital Arts
#   Electrical Engineering
#   Mechanical Engineering
#   Industrial & Systems Engineering
#   Civil & Environmental Engineering
#   Biomedical & Health Informatics
#   Rehabilitation Medicine
#   Communication
#   Architecture
#   Psychology
#   Nursing
# 
# Valid masters affiliations:
#   Master of Science in Computer Science & Engineering
#   Master of Science in Human Centered Design & Engineering
#   Master of Science in Information Management
#   Master of Library and Information Science
#   Master of Design
#   Master of Human-Computer Interaction + Design
#   Master of Science in Biomedical & Health Informatics
#   Master of Science in Electrical Engineering
#   Master of Industrial & Systems Engineering
#   Master of Science in Industrial Engineering
#   Master of Science in Mechanical Engineering
#   Master of Science in Engineering
#   Master of Science in Architecture
#   Master of Communication in Digital Media
#   Master of Communication in Communities and Networks
################################################################################
positions:
- title: Associate Professor
  affiliation: Computer Science & Engineering

################################################################################
# A person may have a website. If not, this field should not be present.
#
# web:
# - http://faculty.washington.edu/ajko/
################################################################################

---
