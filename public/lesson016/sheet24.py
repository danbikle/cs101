"""
sheet24.py

Using a service-account,
This script should create a spreadsheet.
Then, it should make the spreadsheet public-readable.

Demo:
python3 sheet24.py
"""

import datetime
import os
import pickle
from googleapiclient.discovery    import build
from oauth2client.service_account import ServiceAccountCredentials
from httplib2                     import Http

# SCOPES  = ['https://www.googleapis.com/auth/spreadsheets']
# secretf_s = os.environ['HOME']+'/sheetsrv_acct_0615.json'
secretf_s = os.environ['HOME']+'/sheetsrv_acct_0616.json'

with open(secretf_s) as fh:
  json_s = fh.read()

print('json_s[:66]:')
print( json_s[:66])

# I s.declare a very permissive scope (for training only):
scopes      = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(secretf_s, scopes)
http_auth   = credentials.authorize(Http())
service     = build('sheets', 'v4', http=http_auth)

print('I should now be authenticated and authorized to use service:')
print(service)

field_s           = 'spreadsheetId,spreadsheetUrl'
body_d            = {'properties':{'title':'spreadsheet from sheet24.py'}}
response_ofcreate = service.spreadsheets().create(fields=field_s, body=body_d).execute()
spreadsheet_id    = response_ofcreate.get('spreadsheetId')
print('I just created spreadsheet; it has an ID:')
print(spreadsheet_id)
spreadsheet_url = response_ofcreate.get('spreadsheetUrl')
print('spreadsheetUrl:')
print( spreadsheet_url)

# I should make the sheet public readable:
drive_service = build('drive', 'v3', http=http_auth)

print('drive_service:')
print( drive_service)
