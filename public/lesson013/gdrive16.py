"""
gdrive16.py

This script should create a folder named: "afolder"
This script should create hello.txt on Linux.
It should upload hello.txt to Google Drive.
And hello.txt should be inside "afolder".

Demo:
python3 gdrive16.py
"""

from googleapiclient.discovery    import build
from googleapiclient.http         import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
from httplib2                     import Http
import os

# I shd declare a very permissive scope (for training only):
scopes      = ['https://www.googleapis.com/auth/drive']
secretf_s   = os.environ['HOME']+'/drivecred.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(secretf_s, scopes)
http_auth   = credentials.authorize(Http())
drive_service = build('drive', 'v3', http=http_auth)

print('I should now be authenticated and authorized to use drive_service:')
print(drive_service)

# I shd create a folder named: "afolder".

folder_metadata = {
    'name': 'afolder',
    'mimeType': 'application/vnd.google-apps.folder'
}
    
print('folder_metadata:')
print( folder_metadata)

folder_response = drive_service.files().create(body=folder_metadata,
                                    fields='id').execute()
print('folder_response:')
print( folder_response  )

# I s.get the id of the folder so I can use it later:
folder_id = folder_response.get('id')
print('Folder ID: ' + folder_id)

# I shd create /tmp/hello.txt on Linux:
with open('/tmp/hello.txt','w') as fh:
    fh.write("hello world\n")

# I shd upload hello.txt to Google Drive into folder_id:
file_metadata = {'name': 'hello.txt', 'parents': [folder_id]}

media = MediaFileUpload('/tmp/hello.txt', mimetype='text/plain')
print('I will try to upload /tmp/hello.txt to google drive into folder_id:')
create_response = drive_service.files().create(body=file_metadata,
                                     media_body=media,
                                     fields='id').execute()
file_id = create_response.get('id')
print('new /tmp/hello.txt file_id:')
print(file_id)

# I shd "list" hello.txt:

# Q: With googleapiclient, how to filter files list results?
# A1: https://developers.google.com/drive/api/v3/reference/files/list
# A2: https://developers.google.com/drive/api/v3/search-files

list_results = drive_service.files().list(
    orderBy  = "createdTime desc, name desc",
    q        = "name='hello.txt'",
    pageSize = 22,
    fields   = "files(id, name)"
).execute()

items = list_results.get('files', [])

if items:
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))
else:
    print('No files found.')
