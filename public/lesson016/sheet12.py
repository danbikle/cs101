"""
sheet12.py

This script should test an OAuth session from a Python-pickle file.

Demo:
python3 sheet12.py
"""

import os
import pickle
from googleapiclient.discovery import build

SCOPES  = ['https://www.googleapis.com/auth/spreadsheets']
pcklf_s = os.environ['HOME']+'/secret0612.pickle'

with open(pcklf_s, 'rb') as fh:
  creds = pickle.load(fh)
            
print('OAuth session obtained from Python-pickle file:')
print(pcklf_s)
