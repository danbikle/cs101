"""
sheet20.py

This script should use a service-accoount to 
create a sheets-service after authentication.

Demo:
python3 sheet20.py
"""

import datetime
import os
import pickle
from googleapiclient.discovery    import build
from oauth2client.service_account import ServiceAccountCredentials
from httplib2                     import Http

SCOPES  = ['https://www.googleapis.com/auth/spreadsheets']
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
#drive_service = build('drive', 'v3', http=http_auth)
service     = build('sheets', 'v4', http=http_auth)

print('I should now be authenticated and authorized to use service:')
print(service)
