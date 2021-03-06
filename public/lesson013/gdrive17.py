"""
gdrive17.py

This script should create hello.txt on Linux.
It should copy hello.txt to Google Drive.
It should download hello.txt from Google Drive to /tmp/hello2.txt

Demo:
python3 gdrive17.py
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

# I shd download hello.txt:

request    = drive_service.files().get_media(fileId=file_id)
fh         = io.FileIO('/tmp/hello2.txt', 'wb')
downloader = MediaIoBaseDownload(fh, request)
done       = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))

