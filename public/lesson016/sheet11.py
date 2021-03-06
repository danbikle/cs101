"""
sheet11.py

This script helps me see if I setup OAuth okay using steps I list in lesson016.

Demo:
python3 sheet11.py
"""

import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES  = ['https://www.googleapis.com/auth/spreadsheets.readonly']
jsonf_s = os.environ['HOME']+'/secret0612.json'
flow    = InstalledAppFlow.from_client_secrets_file(jsonf_s, SCOPES)
creds   = flow.run_local_server()
