"""
sheet13.py

This script should test an OAuth session from a Python-pickle file.

Demo:
python3 sheet13.py
"""

import os
import pickle
from googleapiclient.discovery import build

SCOPES  = ['https://www.googleapis.com/auth/spreadsheets']
pcklf_s = os.environ['HOME']+'/secret0612.pickle'

with open(pcklf_s, 'rb') as fh:
  creds = pickle.load(fh)
            
print('OAuth session obtained from Python-pickle file:')
print(pcklf_s)

service           = build('sheets', 'v4', credentials=creds)
field_s           = 'spreadsheetUrl'
body_d            = {'properties':{'title':'lesson016sheetA'}}
response_ofcreate = service.spreadsheets().create(fields=field_s, body=body_d).execute()
spreadsheet_id    = response_ofcreate.get('spreadsheetId')
print('I just created spreadsheet; it has an ID:')
print(spreadsheet_id)
spreadsheet_url = response_ofcreate.get('spreadsheetUrl')
print('spreadsheetUrl:')
print( spreadsheet_url)
