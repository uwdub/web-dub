#
# build-faculty-profiles.py
#
# Convert a CSV file of faculty information to Markdown files appropriate for
# consumption by Jekyll.
#

# NOTE: This script is very sensitive to the naming of fields in Google Forms.
#       Namely, the Title and Affiliation fields need to start with the words
#       Title and Affiliation, respectively, and need to contain a sequential
#       index at the end of the field name. If we change the name of those 
#       fields on the form, this script might break.
# TODO: It would be better if we could use some kind of internal field name that
#       is independenet of the user-facing field name. But it's unclear whether 
#       this is possible in Google Forms.

import invoke
import csv
import requests
from jinja2 import Environment, FileSystemLoader

FACULTY_CSV_URL = 'https://docs.google.com/spreadsheets/export?format=csv&id=1WW7S0t6qUcFabLL4I9bE1uLex8wQmA40KfNEfXqCma4'
OUTPUT_DIR = './_people/faculty-new/'
NUM_POSITION_BLOCKS_MAX = 4

def normalize(*args, sep="_"):
  return sep.join(args).lower().replace(' ', sep)

@invoke.task()
def build_faculty_profiles():
  env = Environment(
    loader=FileSystemLoader(searchpath='./_people'),
    trim_blocks = True,
    lstrip_blocks = True
  )
  template = env.get_template('_template.j2')
  csv_file = requests.get(FACULTY_CSV_URL).text.splitlines();
  reader = csv.reader(csv_file, delimiter=',')
  headers = next(reader)

  # loop over all rows in the spreadsheet
  for row in reader:

    # context object to feed to the jinja2 template
    ctx = {
      'role': 'faculty',
      'positions': [{} for _ in range(NUM_POSITION_BLOCKS_MAX)],

      # TODO: determine TBD fields, which will depend on which fields we require
      #       via the input form.
      'tbds': []
    }

    # add data for each field to our context object
    for i in range(len(headers)):
      header = normalize(headers[i])

      # title and affiliation blocks need to be combined into a 'position'
      # object, one for each set of titles and affiliations
      if header.startswith('title') or header.startswith('affiliations'):

        # titles and affiliations are numbered with an index at the end of the
        # header name
        idx = int(header.split('_')[-1]) - 1
        ctx['positions'][idx][header.split('_')[0]] = row[i].strip()
      else:
        ctx[header] = row[i].strip()

    for i in range(len(ctx['positions'])):

      # convert the comma-separated string of affiliations for each position 
      # block into an array, if it exists
      ctx['positions'][i]['affiliations'] = \
        [affil.strip() for affil in ctx['positions'][i]['affiliations'].split(',')]

    # remove any unused title/affiliation blocks
    ctx['positions'].remove({'title': '', 'affiliations': ['']})


    outfile = normalize(ctx['last_name'], ctx['first_name'], sep="-") + '.md'
    print(ctx)
    with open(OUTPUT_DIR + outfile, 'w') as fhand:
      fhand.write(template.render(ctx))
      fhand.close()
