"""
gdrive18.py

This script should create hello.txt on Linux.
It should copy hello.txt to Google Drive.
It should list info about permissions.

Ref:
https://developers.google.com/drive/api/v3/reference/files#methods

Demo:
python3 gdrive18.py
"""

from googleapiclient.discovery    import build
from googleapiclient.http         import MediaFileUpload
from googleapiclient.http         import MediaIoBaseDownload
from oauth2client.service_account import ServiceAccountCredentials
from httplib2                     import Http
import io
import os

# I shd declare a very permissive scope (for training only):
scopes      = ['https://www.googleapis.com/auth/drive']
secretf_s   = os.environ['HOME']+'/drivecred.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(secretf_s, scopes)
http_auth   = credentials.authorize(Http())
drive_service = build('drive', 'v3', http=http_auth)

print('I should now be authenticated and authorized to use drive_service:')
print(drive_service)

# I shd create /tmp/hello.txt on Linux:
with open('/tmp/hello.txt','w') as fh:
    fh.write("hello world\n")

# I shd copy hello.txt to Google Drive.
file_metadata = {'name': 'hello.txt'}
media = MediaFileUpload('/tmp/hello.txt', mimetype='text/plain')
print('I will try to upload /tmp/hello.txt to google drive:')
create_response = drive_service.files().create(body=file_metadata,
                                     media_body=media,
                                     fields='id').execute()
file_id = create_response.get('id')
print('new /tmp/hello.txt file_id:')
print(file_id)

perm_response = drive_service.permissions().list(fileId=file_id).execute()
print('perm_response:')
print( perm_response)


