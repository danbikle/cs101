"""
googdrive17.py

This script should delete files named 'hello.txt'

Ref:
https://developers.google.com/drive/api/v3/quickstart/python

Demo (Ubuntu):
sudo apt install python3-pip
sudo pip3 install --upgrade google-api-python-client
sudo pip3 install --upgrade google-auth-httplib2
sudo pip3 install --upgrade google-auth-oauthlib

python3 googdrive17.py
"""

import pickle
import os.path
from googleapiclient.discovery      import build
from googleapiclient.http           import MediaFileUpload
from google_auth_oauthlib.flow      import InstalledAppFlow
from google.auth.transport.requests import Request

# I s.declare a very permissive scope (for training only):
SCOPES      = ['https://www.googleapis.com/auth/drive']

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as fh:
        creds = pickle.load(fh)
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

# I s.create a file so I can upload it:
with open('/tmp/hello.txt','w') as fh:
    fh.write("hello world\n")
# From my laptop, I s.upload a file named hello.txt:
drive_service = build('drive', 'v3', credentials=creds)
file_metadata = {'name': 'hello.txt'}
media = MediaFileUpload('/tmp/hello.txt', mimetype='text/plain')
create_response = drive_service.files().create(body=file_metadata,
                                     media_body=media,
                                     fields='id').execute()
file_id = create_response.get('id')
print('new /tmp/hello.txt file_id:')
print(file_id)

# Q: With googleapiclient, how to filter files list()-response?
# A1: https://developers.google.com/drive/api/v3/reference/files/list
# A2: https://developers.google.com/drive/api/v3/search-files

list_response = drive_service.files().list(
    orderBy   = "createdTime desc",
    q         = "name='hello.txt'",
    pageSize  = 22,
    fields    = "files(id, name)"
).execute()

items = list_response.get('files', [])

if items:
    for item in items:
        print('I will try to delete this file:')
        print(u'{0} ({1})'.format(item['name'], item['id']))
        del_response = drive_service.files().delete(fileId=item['id'])
        print('del_response.body:')
        print( del_response.body)
    print('I will try to emptyTrash:')
    trash_response = drive_service.files().emptyTrash()
    print('trash_response.body:')
    print( trash_response.body)
else:
    print('hello.txt not found in your google-drive account.')

