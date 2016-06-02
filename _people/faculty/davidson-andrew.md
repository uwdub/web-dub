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
# - Surname
# - First
# - Middle
# - More
################################################################################
name:
- Davidson
- Andrew

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
- title: Senior Lecturer
  unit: Human Centered Design & Engineering
- title: Adjunct Senior Lecturer
  unit: Division of Design

################################################################################
# A person may have a website. If not, this field should not be present.
#
# web:
# - http://faculty.washington.edu/ajko/
################################################################################
web:
- http://faculty.washington.edu/adavid7

############################################################
# These fields are provided to ease migration of old content.
# They are not used, and should be deleted when no longer desired.
old-dub-bio: "Andrew Davidson is a Senior Lecturer in the Department of Human-Centered\
  \ Design & Engineering and Director of the HCDE Educational Labs. His current research\
  \ centers on physical computing applications, creating interactive objects and environments\
  \ with open-source electronics and software prototyping platforms.\r\n\r\nDavidson\
  \ is a technologist and designer who has worked in a wide variety of professional\
  \ and educational contexts. Over the last 30 years, he has developed, managed, and\
  \ communicated about innovative technology projects in human-centered interactive\
  \ systems. These include ground-breaking computer graphics for motion pictures,\
  \ early interactive television experiments, and interactive projects with artists,\
  \ designers and commercial clients. \r\n\r\nAs an educator, Davidson has taught\
  \ in and overseen leading international research-oriented design technology programs\
  \ (Art Center College of Design, Interaction Design Institute Ivrea, University\
  \ of Washington\u2019s Division of Design). He has also taught high school computer\
  \ science and done STEM outreach in secondary education."
old-dub-photo: icons/people/pelato.gif
twitter:
- ahdavidson7
---
