#
# build-faculty-profiles.py
#
# Convert a CSV file of faculty information to Markdown files appropriate for
# consumption by Jekyll.
#

# NOTE: This script is very sensitive to the naming of fields in Google Forms.
#       Namely, the Title, Affiliation, and Name fields need to start with the 
#       words Title, Affiliation, and Name, respectively, and need to contain a 
#       sequential index at the end of the field name. If we change the name of 
#       those fields on the form, this script might break.
# TODO: It would be better if we could use some kind of internal field name that
#       is independenet of the user-facing field name. But it's unclear whether 
#       this is possible in Google Forms.

import invoke
import csv
import requests
import imghdr
import re
from os import rename
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader

FACULTY_CSV_URL = 'https://docs.google.com/spreadsheets/export?format=csv&id=1WW7S0t6qUcFabLL4I9bE1uLex8wQmA40KfNEfXqCma4'
OUTPUT_DIR = './_people/faculty-new/'
NUM_POSITION_BLOCKS_MAX = 4
NUM_NAME_FIELDS_MAX = 5

# join together any number of strings, replacing all whitespace with sep,
# converting to lowercase, and stripping out non-alphanumeric characters
def normalize(fields, sep="_"):
  fields = [fields] if not type(fields) is list else fields
  regex = '[^A-Za-z0-9\\' + sep + ']'
  return re.sub(regex, '', sep.join(fields).lower().replace(' ', sep))

# certain fields--like title, affiliation, and name--have a sequential index in
# the header. This function pulls that index out for use
def get_field_index(field):
  return int(field.split('_')[-1]) - 1

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
      'name': ['' for _ in range(NUM_NAME_FIELDS_MAX)],

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
        ctx['positions'][get_field_index(header)][header.split('_')[0]] = row[i].strip()

      # names can consist of several fields
      elif header.startswith('name'):
        ctx['name'][get_field_index(header)] = row[i].strip()
      else:
        ctx[header] = row[i].strip()

    for i in range(len(ctx['positions'])):

      # convert the comma-separated string of affiliations for each position 
      # block into an array, if it exists
      ctx['positions'][i]['affiliations'] = \
        [affil.strip() for affil in ctx['positions'][i]['affiliations'].split(',')]

    # remove any unused title/affiliation and name blocks
    ctx['positions'].remove({'title': '', 'affiliations': ['']})
    ctx['name'].remove('')

    outfile_base = normalize(ctx['name'], sep='-')
    with open(OUTPUT_DIR + outfile_base + '.md', 'w') as fhand:
      fhand.write(template.render(ctx))
      fhand.close()

    # fetch and save raw profile image
    if ctx['profile_picture']:

      # reformat the google drive url for downloading
      parsed_url = urlparse(ctx['profile_picture'])
      parsed_qs = parse_qs(parsed_url.query)
      file_id = parsed_qs['id'][0]
      url = 'https://drive.google.com/uc?export=download&id=' + file_id
      response = requests.get(url)

      if response.status_code == 200:
        path = OUTPUT_DIR + outfile_base + '-raw'
        with open(path, 'wb') as fhand:
          fhand.write(response.content)
          fhand.close()
          file_type = imghdr.what(path)
          rename(path, path + '.' + file_type)
          
