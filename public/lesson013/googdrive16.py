"""
googdrive16.py

This script should delete files named 'hello.txt'

ref:
https://stackoverflow.com/questions/46457093/google-drive-api-with-python-from-serverbackend-without-browser-autentication

I s.use this URL to enable drive-API for my project:
https://console.cloud.google.com/apis/library/drive.googleapis.com
I s.use this URL to download secret.json from the default service-account:
https://console.developers.google.com/iam-admin/serviceaccounts
I s.copy the json-key-file to $HOME/secret.json

Demo:
pip3 install oauth2client
python3 googdrive16.py
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
        print('I will attempt to delete this file:')
        print(u'{0} ({1})'.format(item['name'], item['id']))
        del_results = drive_service.files().delete(fileId=item['id']).execute()
        print(del_results)
    print('I will attempt to emptyTrash:')
    trash_results = drive_service.files().emptyTrash().execute()
    print('trash_results:')
    print( trash_results)
else:
    print('No files found.')
