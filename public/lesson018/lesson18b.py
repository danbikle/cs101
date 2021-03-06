"""
lesson18b.py

This script should:

- Create a file named hello.txt
- Copy hello.txt to Google Drive
- Grant reader-role to anyone (who wants it)
- Grant writer-role to bikle101@gmail.com

Demo:
python3 lesson18b.py
"""

import os
from googleapiclient.discovery    import build
from googleapiclient.http         import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
from httplib2                     import Http

secretf_s = os.environ['HOME']+'/secret0822.json'

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

# I shd create /tmp/hello.txt on Linux:
with open('/tmp/hello.txt','w') as fh:
    fh.write("hello world\n")

# I shd copy hello.txt to Google Drive.
file_metadata = {'name': 'hello.txt'}
media = MediaFileUpload('/tmp/hello.txt', mimetype='text/plain')
print('I will try to upload /tmp/hello.txt to google drive:')
create_response = service.files().create(body=file_metadata,
                                     media_body=media,
                                     fields='id').execute()
file_id = create_response.get('id')
print('new /tmp/hello.txt file_id:')
print(file_id)

# I shd grant reader-role to anyone (who wants it):
newperm_d   = {'role': 'reader', 'type': 'anyone'}
pc_response = service.permissions().create(fileId=file_id,
                                                   body=newperm_d
).execute()

print('pc_response:')
print( pc_response)

# I shd grant writer-role to bikle101@gmail.com:
newperm_d   = {'role': 'writer', 'type': 'user',
               'emailAddress': 'bikle101@gmail.com'}

pc_response = service.permissions().create(fileId=file_id,
                                           body=newperm_d
).execute()

print('pc_response:')
print( pc_response)

response_ofget = service.files().get(fileId=file_id,fields='webViewLink'
).execute()

print('The URL of the file, hello.txt, is:')
print(response_ofget['webViewLink'])
