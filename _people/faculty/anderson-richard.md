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
- Anderson
- Richard

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
#  role:
#  - faculty
#  position:
#  - title: Professor
#    unit: Information School
#  - title: Professor
#    unit: Computer Science & Engineering
# 
# Students do not have a title, but can have one more units.
#
# For a doctoral student their unit is the name of their department.
#  role:
#  - doctoral-student
#  position:
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
- title: Professor
  unit: Computer Science & Engineering

################################################################################
# A person may have a website. If not, this field should not be present.
#
# web:
# - http://faculty.washington.edu/ajko/
################################################################################
web:
- http://www.cs.washington.edu/people/faculty/anderson

############################################################
# These fields are provided to ease migration of old content.
# They are not used, and should be deleted when no longer desired.
old-dub-bio: "<b> Richard Anderson</b> is a Professor in the Department of Computer\
  \ Science and Engineering at the University \r\nof Washington.  He graduated with\
  \ a B.A. in\r\nMathematics from <a href=\"http://www.reed.edu/\"> Reed College </a>\
  \ in 1981,\r\nand a Ph.D. in Computer Science from <a href=\"http://www.cs.stanford.edu\"\
  >Stanford University</a>\r\nin 1985.  He joined the <a href=\"http://www.washington.edu\"\
  >University of Washington</a> in 1986, after a\r\none-year Postdoc at the <a href=\"\
  http://www.msri.org\"> Mathematical Science \r\nResearch Institute </a> in\r\nBerkeley,\
  \ CA.  In 1987 he received an NSF Presidential Young\r\nInvestigator award.  He\
  \ spent the 1993-1994 academic year\r\nas a visiting professor at the <a href=\"\
  http://www.iisc.ernet.in/\"> \r\nIndian Institute of Science</a>, in Bangalore,\
  \ India, and the 2001-2002 academic year a visiting researcher in the \r\nLearning\
  \ Sciences and Technology group at <a \r\nhref=\"http://research.microsoft.com\"\
  >Microsoft Research</a>.  While at Microsoft, he led the development of <a \r\n\
  href=\"http://www.cs.washington.edu/education/dl/presenter/\">Classroom Presenter</a>,\
  \ a tool for delivering presentations from the \r\nTabletPC.  He was the 2007 recipient\
  \ of the UW College of Engineering\r\nFaculty Innovator for Teaching Award.  He\
  \ has been the department's assoicate chair for educational programs since 2004.\r\
  \n </p>\r\n\r\n<P>\r\nRichard Anderson's main research interests are in Computing\
  \ for the Developing World,   Educational Technology, and Pen Based Computing. He\
  \ is \r\nparticularly interested in using technology to improve the classroom environment,\
  \ and in educational applications of \r\n\r\nthe Tablet PC.  Previously, he has\
  \ worked in the theory and implementation\r\nof algorithms, including parallel algorithms,\
  \ computational geometry, and \r\nscientific applications.   He was a founder of\
  \ the department's <a \r\nhref=\"http://www.cs.washington.edu/masters/\">Professional\
  \ Master's Program</a> and led the effort to export the department's introductory\
  \ programming courses using <a href=http://www.cs.washington.edu/education/TVI/>Tutored\
  \ \r\nVideo Instruction</a>. \r\n"
old-dub-photo: icons/people/rja.jpg
---
