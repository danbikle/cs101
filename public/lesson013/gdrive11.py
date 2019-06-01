"""
gdrive11.py

This script should confirm that Python could read ~/drivecred.json.
And I should be able to import googleapiclient

Demo:
cp ~/Downloads/drivecred.json ~
python3 gdrive11.py
"""

import os

print("os.environ['HOME']:")
print( os.environ['HOME'])

with open(os.environ['HOME'] + '/drivecred.json') as fh:
    drivecred_json_s = fh.read()

print(os.environ['HOME'] + '/drivecred.json' + ' has this JSON inside:')
print(drivecred_json_s[:79] + ' ...')

import googleapiclient
