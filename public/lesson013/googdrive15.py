"""
googdrive15.py

ref:
https://stackoverflow.com/questions/46457093/google-drive-api-with-python-from-serverbackend-without-browser-autentication

I s.use this URL to enable drive-API for my project:
https://console.cloud.google.com/apis/library/drive.googleapis.com
I s.use this URL to download secret.json from the default service-account:
https://console.developers.google.com/iam-admin/serviceaccounts
I s.copy the json-key-file to $HOME/secret.json

Demo:
pip3 install oauth2client
python3 googdrive15.py
"""

from googleapiclient.discovery    import build
from googleapiclient.http         import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
from httplib2                     import Http
import os

# I s.declare a very permissive scope (for training only):
scopes      = ['https://www.googleapis.com/auth/drive']
secretf_s   = os.environ['HOME']+'/secret.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(secretf_s, scopes)
http_auth   = credentials.authorize(Http())
drive_service = build('drive', 'v3', http=http_auth)

folder_metadata = {
    'name': 'afolder',
    'mimeType': 'application/vnd.google-apps.folder'
}
    
folder    = drive_service.files().create(body=folder_metadata, fields='id').execute()
folder_id = folder.get('id')
print('folder_id:')
print(folder_id)

# I s.create a file so I can upload it:
with open('/tmp/hello.txt','w') as fh:
    fh.write("hello world\n")
    
file_metadata = {
    'name': 'hello.txt',
    'parents': [folder_id]
}
# From my laptop, I s.upload a file named hello.txt:
media = MediaFileUpload('/tmp/hello.txt', mimetype='text/plain')
file  = drive_service.files().create(body=file_metadata,
                                     media_body=media,
                                     fields='id').execute()
file_id = file.get('id')
print('file_id:')
print(file_id)

# Call the Drive v3 API
results = drive_service.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
print('results:')
#print(results)
items = results.get('files', [])

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))        
