"""
sheet15.py

This script should create a spreadsheet, then call 
service.spreadsheets().values().batchUpdate()

This script should do the same as sheet14.py except 
use batchUpdate() instead of update().

Demo:
python3 sheet15.py
"""

import datetime
import os
import pickle
from googleapiclient.discovery import build

SCOPES  = ['https://www.googleapis.com/auth/spreadsheets']
pcklf_s = os.environ['HOME']+'/secret0612.pickle'

with open(pcklf_s, 'rb') as fh:
  creds = pickle.load(fh)
            
print('OAuth session obtained from Python-pickle file:')
print(pcklf_s)

# I shd get a UTC timestamp-string for the spreadsheet title:
my_dt = datetime.datetime.utcnow()
my_s  = datetime.datetime.strftime(my_dt, '%Y-%m-%d %H:%M:%S')

title_s           = 'lesson016sheet ' + my_s
service           = build('sheets', 'v4', credentials=creds)
field_s           = 'spreadsheetUrl,spreadsheetId'
body_d            = {'properties':{'title':title_s}}
response_ofcreate = service.spreadsheets().create(fields=field_s
                                                  ,body=body_d).execute()
spreadsheet_id    = response_ofcreate.get('spreadsheetId')
print('I just created spreadsheet; it has an ID:')
print(spreadsheet_id)
spreadsheet_url = response_ofcreate.get('spreadsheetUrl')
print('spreadsheetUrl:')
print( spreadsheet_url)

range_s  = 'Sheet1!A1' # The range in A1 notation
row1_l   = [1.1, 2.1, 3.3]
row2_l   = [1.2, 2.3, 3.1]
values_l = [row1_l, row2_l] # A nested list full of values

# I shd combine range_s and values_l into a list of dictionaries:
data_l = [
  {
    'range':  range_s,
    'values': values_l
  } # just 1 dictionary for now
]

body_d = {
  'valueInputOption': 'USER_ENTERED',
  'data': data_l
} # Another dictionary for batchUpdate()

response_ofbatchUpdate = service.spreadsheets().values().batchUpdate(
  spreadsheetId=spreadsheet_id,
  body = body_d).execute()

print("response_ofbatchUpdate.get('totalUpdatedCells'):")
print( response_ofbatchUpdate.get('totalUpdatedCells')  )
