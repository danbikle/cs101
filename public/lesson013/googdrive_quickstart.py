"""
googdrive_quickstart.py

This script should use python3 to talk with Google Drive.

Ref:
https://developers.google.com/drive/api/v3/quickstart/python

The above URL offers a blue button [ENABLE THE DRIVE API] to get credentials.json

I placed my copy of credentials.json here: $HOME/credentials.json

Demo:
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 google_drive_quickstart.py
"""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        print("os.path.exists('token.pickle')")
        with open('token.pickle', 'rb') as token:
            print('creds = pickle.load(token)')
            creds = pickle.load(token)
            print('creds:')
            print(creds)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        print('not creds or not creds.valid')
        if creds and creds.expired and creds.refresh_token:
            print('creds and creds.expired and creds.refresh_token')
            creds.refresh(Request())
        else:
            print('getting flow')
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            print('getting creds')
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            print('pickle.dump(creds, token)')
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    print('service:')
    print(service)

    # Call the Drive v3 API
    results = service.files().list(
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
        
if __name__ == '__main__':
    print('Calling main()...')
    main()
    
print('Done')
