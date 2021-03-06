"""
sheet12.py

This script should demo some of the Google Sheets API.

Ref:
https://developers.google.com/sheets/api/quickstart/python

Demo:
python3 sheet12.py
"""

import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME     = 'Class Data!A2:E'

SCOPES  = ['https://www.googleapis.com/auth/spreadsheets.readonly']
jsonf_s = os.environ['HOME']+'/secret0611.json'
flow    = InstalledAppFlow.from_client_secrets_file(jsonf_s, SCOPES)
creds   = flow.run_local_server()

print('I should be authenticated now:')
print(creds)

print('I should build a service:')
service = build('sheets', 'v4', credentials=creds)
print(service)

# Call the Sheets API
sheet  = service.spreadsheets()
print('I should find values in the spreadsheet.')
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

if values:
  print('len(values):')
  print( len(values))
  print('Name, Major:')
  for row in values:
    # Print columns A and E, which correspond to indices 0 and 4.
    print('%s, %s' % (row[0], row[4]))
else:
  print('I found no values in the spreadsheet; bye.')
