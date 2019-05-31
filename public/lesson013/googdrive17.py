"""
googdrive17.py

This script should delete files named 'hello.txt'

Demo:
python3 googdrive17.py
"""

from googleapiclient.discovery    import build
#from googleapiclient.http         import MediaFileUpload
import os

import pickle
import os.path
from google_auth_oauthlib.flow      import InstalledAppFlow
from google.auth.transport.requests import Request


# I s.declare a very permissive scope (for training only):
scopes      = ['https://www.googleapis.com/auth/drive']

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as fh:
        creds = pickle.load(fh)
'''
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

drive_service = build('drive', 'v3', credentials=creds)

# Q: With googleapiclient, how to filter files list results?
# A1: https://developers.google.com/drive/api/v3/reference/files/list
# A2: https://developers.google.com/drive/api/v3/search-files

list_results = drive_service.files().list(
    orderBy  = "createdTime desc",
    q        = "name='hello.txt'",
    pageSize = 22,
    fields   = "files(id, name)"
).execute()

items = list_results.get('files', [])

if items:
    print('Files I want to delete:')
    for item in items:
        print('I will attempt to delete this file:')
        print(u'{0} ({1})'.format(item['name'], item['id']))
        del_results = drive_service.files().delete(fileId=item['id'])
        print(del_results.body)
    print('I will attempt to emptyTrash:')
    trash_results = drive_service.files().emptyTrash()
    print('trash_results.body:')
    print( trash_results.body)
else:
    print('No files found.')
'''
