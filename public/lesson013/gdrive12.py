"""
gdrive12.py

This script should confirm that Python can authenticate to gdrive using ~/drivecred.json.

Demo:
sudo apt install python3-pip
sudo pip3 install google-api-python-client
sudo pip3 install oauth2client
sudo pip3 install google-auth-oauthlib      
python3 gdrive12.py
"""

from googleapiclient.discovery    import build
from googleapiclient.http         import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
from httplib2                     import Http
import os

print("os.environ['HOME']:")
print( os.environ['HOME'])

with open(os.environ['HOME'] + '/drivecred.json') as fh:
    drivecred_json_s = fh.read()

print(os.environ['HOME'] + '/drivecred.json' + ' has this JSON inside:')
print(drivecred_json_s[:79] + ' ...')

# I s.declare a very permissive scope (for training only):
scopes      = ['https://www.googleapis.com/auth/drive']
secretf_s   = os.environ['HOME']+'/drivecred.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(secretf_s, scopes)
http_auth   = credentials.authorize(Http())
drive_service = build('drive', 'v3', http=http_auth)

print('I should now be authenticated and authorized to use drive_service:')
print(drive_service)



