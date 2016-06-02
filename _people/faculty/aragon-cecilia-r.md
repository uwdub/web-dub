---
################################################################################
# Version of the people format. The only valid value for this is 1. 
# We may increment this in the future to simplify maintenance of old people.
################################################################################
version: 1

################################################################################
# A people file might exist but lack values for some fields. These are 'NA'. 
# The only valid value is 'True'. A NA field should not be present if 'False'.
################################################################################
na_web: true

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
- Aragon
- Cecilia
- R.

################################################################################
# Each person has a single main role, and may have additional alumni roles.
# The first role that is listed is their main (current) role.
# Valid roles: faculty, doctoral, masters, undergrad, staff
#              alumni-faculty, alumni-doctoral, alumni-masters, alumni-undergrad
#
# A person may have multiple positions. Positions consist of titles and units.
# Each value for a field must match one of the options below exactly.
#
# Valid faculty titles: Professor, Professor Emeritus
#
# Valid faculty and doctoral units:
#   Computer Science & Engineering
#   Division of Design
#   Human Centered Design & Engineering
#   Information School
#   Human Computer Interaction & Design
#   Architecture
#   Biomedical & Health Informatics
#   Communications
#   DXARTS Digital Arts
#   Electrical Engineering
#   Industrial & Systems Engineering
#   Mechanical Engineering
#   Electrical Engineering
#   Psychology
# 
# Valid masters units:
#   Master of Science in Computer Science & Engineering
#   Master of Design
#   Master of Science in Human Centered Design & Engineering
#   Master of Science in Information Management
#   Master of Library and Information Science
#   Master of Human-Computer Interaction + Design
#   Master of Science in Architecture
#   Master of Science in Biomedical and Health Informatics
#   Master of Communication in Digital Media
#   Master of Communication in Communities and Networks
#   Master of Science in Electrical Engineering
#   Master of Industrial and Systems Engineering
#   Master of Science in Industrial Engineering
#   Master of Science in Mechanical Engineering
#   Master of Science in Engineering
#
# Faculty have one or more title and units.
# role:
#  - faculty
# position:
#  - title: Professor
#    unit: Information School
#  - title: Professor
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
################################################################################
role:
- faculty

position:
- title: Associate Professor
  unit: Human Centered Design & Engineering
- title: Adjunct Professor
  unit: Computer Science & Engineering
- title: Adjunct Professor
  unit: Electrical Engineering
- title: Adjunct Professor
  unit: Information School

################################################################################
# A person may have a website. If not, this field should not be present.
#
# web:
# - http://faculty.washington.edu/ajko/
################################################################################
web:
- http://faculty.washington.edu/aragon/

############################################################
# These fields are provided to ease migration of old content.
# They are not used, and should be deleted when no longer desired.
old-dub-bio: Cecilia Aragon is an Associate Professor in the Department of Human Centered
  Design &amp; Engineering, with adjunct appointments in the Department of Computer
  Science &amp; Engineering and the Information School. Her research focuses on information
  visualization, applications to scientific collaborations, eScience, and computer-supported
  cooperative work (CSCW). Prior to coming to the University of Washington, Professor
  Aragon was a computer scientist at Lawrence Berkeley National Laboratory in Berkeley,
  CA and NASA Ames Research Center in Mountain View, CA. She holds a Ph.D. in computer
  science from the University of California, Berkeley, and a B.S. in mathematics from
  the California Institute of Technology.
old-dub-photo: icons/people/aragon108x142.jpg
---
