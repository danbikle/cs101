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
field_s           = 'spreadsheetUrl,spreadsheetId'
body_d            = {'properties':{'title':'lesson016sheetB'}}
response_ofcreate = service.spreadsheets().create(fields=field_s, body=body_d).execute()
response_ofget    = response_ofcreate.get('spreadsheetId')
print('I just created spreadsheet; it has an ID:')
print(response_ofget)

# To write I need this:
# spreadsheetId
# The range in A1 notation
# some data

# I shd use a spreadsheets.values.update request to write data to a single range

row1_l   = [1.1, 2.1, 3.3]
row2_l   = [1.2, 2.3, 3.1]
values_l = [row1_l, row2_l]
