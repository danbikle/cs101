"""
googdrive13.py

This script should use python3 to talk with Google Drive.

Ref:
https://developers.google.com/drive/api/v3/quickstart/python

The above URL offers a blue button [ENABLE THE DRIVE API] to get credentials.json

I placed my copy of credentials.json here: $HOME/credentials.json

Demo:
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 googdrive13.py
"""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery      import build
from googleapiclient.http           import MediaFileUpload
from google_auth_oauthlib.flow      import InstalledAppFlow
from google.auth.transport.requests import Request
import subprocess

# I s.download a large file which I will upload later:
# /usr/bin/curl https://repo.continuum.io/archive/Anaconda3-2019.03-Linux-x86_64.sh --output /tmp/Anaconda3-2019.03-Linux-x86_64.sh

largef_s = 'Anaconda3-2019.03-Linux-x86_64.sh'
url_s    = 'https://repo.continuum.io/archive/' + largef_s
sub_l    = ['/usr/bin/curl', url_s, '--output', '/tmp/'+largef_s]
print('Waiting for this to finish:')
print(sub_l)
subprocess.run(['/usr/bin/curl', url_s, '--output', '/tmp/'+largef_s])

# If modifying these scopes, delete the file token.pickle.
# Less permissions:
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
# MORE permissions:
SCOPES = ['https://www.googleapis.com/auth/drive']
# Info about scopes:
# https://developers.google.com/drive/api/v3/about-auth

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first time.
if os.path.exists('/tmp/token.pickle'):
    with open('/tmp/token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            os.environ['HOME']+'/credentials.json', SCOPES)
        creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('/tmp/token.pickle', 'wb') as token:
        pickle.dump(creds, token)

drive_service = build('drive', 'v3', credentials=creds)
# Call the Drive v3 API
# Create a folder.
# Ref:
# https://developers.google.com/drive/api/v3/folder

file_metadata = {
    'name': 'Invoices',
    'mimeType': 'application/vnd.google-apps.folder'
}
    
print('file_metadata:')
print( file_metadata)

file = drive_service.files().create(body=file_metadata,
                                    fields='id').execute()

# I s.get the id of the folder so I can use it later:
folder_id = file.get('id')
print('Folder ID: %s' % folder_id)
# Q: How to delete a folder?

file_metadata = {
    'name': 'Anaconda3-2019.03-Linux-x86_64.sh',
    'parents': [folder_id]
}

media = MediaFileUpload('/tmp/Anaconda3-2019.03-Linux-x86_64.sh',
                        mimetype='application/x-sh',
                        chunksize=1024*1024,
                        resumable=True)

request = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()

file_id = request.get('id')

print('File ID: %s' % file_id)

print('Done')
