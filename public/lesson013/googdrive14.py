"""
googdrive14.py

ref:
https://stackoverflow.com/questions/46457093/google-drive-api-with-python-from-serverbackend-without-browser-autentication

https://console.cloud.google.com/apis/library/drive.googleapis.com
https://console.developers.google.com/iam-admin/serviceaccounts

Demo:
python3 googdrive14.py
"""

from googleapiclient.discovery    import build
from oauth2client.service_account import ServiceAccountCredentials
from httplib2                     import Http
import os

# I s.declare a very permissive scope (for training only):
scopes      = ['https://www.googleapis.com/auth/drive']
secretf_s   = os.environ['HOME']+'/secret.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(secretf_s, scopes)
http_auth   = credentials.authorize(Http())
drive       = build('drive', 'v3', http=http_auth)
request     = drive.files().list().execute()
files       = request.get('items', [])
for f in files:
    print(f)
