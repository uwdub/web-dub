#
# build-faculty-profiles.py
#
# Fetch a file of faculty bio information from Google Sheets and convert it
# to Markdown files suitable for consumption by Jekyll. Fetch profile images
# referenced on the spreadsheet and save them locally.
#
# Usage (from root of project): invoke build_faculty_profiles
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
import os
import re
import io
import httplib2
from jinja2 import Environment, FileSystemLoader
from urllib.parse import urlparse, parse_qs
from apiclient import discovery, http as google_http
from oauth2client.service_account import ServiceAccountCredentials


OUTPUT_DIR = './_people/faculty-new/'
# max number of position blocks (title and affiliation) that we allow on the 
# Google form
NUM_POSITION_BLOCKS_MAX = 4
# max number of name fields that we allow on the Google form
NUM_NAME_FIELDS_MAX = 5
GOOGLE_SHEETS_ID = '1WW7S0t6qUcFabLL4I9bE1uLex8wQmA40KfNEfXqCma4'
# the sheet name and column range to use
GOOGLE_SHEETS_RANGE = 'Form Responses 1!A:X'
GOOGLE_CREDENTIALS_PATH = 'secrets/google-api-credentials.json'

# TODO: pull this from a sequence file and keep it up to date
LAST_ACCESSED_ROW = 1

def normalize(fields, sep="_"):
  """
  Join together any number of strings, replacing all whitespace with sep,
  converting to lowercase, and stripping out non-alphanumeric characters
  """
  fields = [fields] if not type(fields) is list else fields
  regex = '[^A-Za-z0-9\\' + sep + ']'
  return re.sub(regex, '', sep.join(fields).lower().replace(' ', sep))


def pluck_field_index(field):
  """
  Certain fields--like title, affiliation, and name--have a sequential index in
  the header. This function pulls that index out for use
  """
  return int(field.split('_')[-1]) - 1


@invoke.task()
def build_faculty_profiles():
  if not os.path.exists(GOOGLE_CREDENTIALS_PATH):
    print('Error: Missing credentials file %s. Aborting.' % GOOGLE_CREDENTIALS_PATH)
    return

  # establish our Google API credentials
  scope = ['https://www.googleapis.com/auth/spreadsheets.readonly']
  credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_PATH, scope)
  http = credentials.authorize(httplib2.Http())

  # fetch data from the spreadsheet
  discovery_url = ('https://sheets.googleapis.com/$discovery/rest?'
                   'version=v4')
  google_service = discovery.build('sheets', 'v4', http=http,
                                   discoveryServiceUrl=discovery_url)
  result = (google_service
            .spreadsheets()
            .values()
            .get(spreadsheetId=GOOGLE_SHEETS_ID, range=GOOGLE_SHEETS_RANGE)
            .execute()
            .get('values', []))
  headers = result[0]

  # set up our jinja2 template
  env = Environment(
    loader=FileSystemLoader(searchpath='./_people'),
    trim_blocks=True,
    lstrip_blocks=True
  )
  template = env.get_template('_template.j2')

  # build portfolios for any new data on the spreadsheet
  new_portfolios = 0
  start_row = LAST_ACCESSED_ROW + 1
  for row in result[start_row:]:

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
    for i in range(len(row)):
      header = normalize(headers[i])
      val = row[i].strip()

      # title and affiliation fields need to be combined into a 'position'
      # block, one for each set of titles and affiliations
      if header.startswith('title') or header.startswith('affiliations'):
        if val:
          ctx['positions'][pluck_field_index(header)][header.split('_')[0]] = val

      # names can consist of several fields
      elif header.startswith('name'):
        if val:
          ctx['name'][pluck_field_index(header)] = val

      else:
        ctx[header] = val

    # filter out any unused position blocks and name fields
    ctx['positions'] = [x for x in ctx['positions'] if x]
    ctx['name'] = [x for x in ctx['name'] if x]

    for i in range(len(ctx['positions'])):

      # convert the comma-separated string of affiliations for each position 
      # block into an array, if it exists
      ctx['positions'][i]['affiliations'] = \
        [affil.strip() for affil in ctx['positions'][i]['affiliations'].split(',')]

    outfile_base = normalize(ctx['name'], sep='-')
    with open(OUTPUT_DIR + outfile_base + '.md', 'w') as fhand:
      fhand.write(template.render(ctx))
      fhand.close()

    new_portfolios += 1

    # fetch and save raw profile image
    if ctx['profile_picture']:

      # pull the image file id out of the saved URL
      parsed_url = urlparse(ctx['profile_picture'])
      parsed_qs = parse_qs(parsed_url.query)
      file_id = parsed_qs['id'][0]

      # establish our Google API credentials
      scope = ['https://www.googleapis.com/auth/drive.readonly']
      credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_PATH, scope)
      http = credentials.authorize(httplib2.Http())

      # fetch raw image from Google Drive
      google_service = discovery.build('drive', 'v3', http=http)
      metadata = google_service.files().get(fileId=file_id).execute()
      file_extension = metadata['mimeType'].split('/')[-1]
      request = google_service.files().get_media(fileId=file_id)
      fhand = io.BytesIO()
      downloader = google_http.MediaIoBaseDownload(fhand, request)
      done = False
      while done is False:
        status, done = downloader.next_chunk()

      with open(OUTPUT_DIR + outfile_base + '-raw.' + file_extension, 'wb') as f:
        f.write(fhand.getvalue())
        f.close()
          
  print("Done! Built %d new faculty portfolios" % new_portfolios)
