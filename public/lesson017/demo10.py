"""
demo10.py

This script should:

- Create a file named hello.txt
- Copy hello.txt to Google Drive
- Grant reader-role to anyone (who wants it)
- Grant writer-role to bikle101@gmail.com

Demo:
python3 demo10.py
"""

import datetime
import os
import pickle
from googleapiclient.discovery    import build
from oauth2client.service_account import ServiceAccountCredentials
from httplib2                     import Http

secretf_s = os.environ['HOME']+'/secret0616.json'

with open(secretf_s) as fh:
  json_s = fh.read()

print('json_s[:66]:')
print( json_s[:66])

# I s.declare a very permissive scope (for training only):
SCOPES      = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(secretf_s,
                                                               SCOPES)
http_auth = credentials.authorize(Http())
service   = build('drive', 'v3', http=http_auth)

print('I should now be authenticated and authorized to use service:')
print(service)
