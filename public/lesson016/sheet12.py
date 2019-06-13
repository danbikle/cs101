"""
sheet12.py

This script should persist an OAuth session to a Python-pickle file.

Demo:
python3 sheet12.py
"""

import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES  = ['https://www.googleapis.com/auth/spreadsheets']
jsonf_s = os.environ['HOME']+'/secret0612.json'
pcklf_s = os.environ['HOME']+'/secret0612.pickle'
flow    = InstalledAppFlow.from_client_secrets_file(jsonf_s, SCOPES)
creds   = flow.run_local_server()

with open(pcklf_s, 'wb') as fh:
  pickle.dump(creds, fh)

print('OAuth session persisted to a Python-pickle file:')
print(pcklf_s)
