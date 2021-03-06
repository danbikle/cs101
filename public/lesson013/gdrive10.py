"""
gdrive10.py

This script should confirm that Python could read ~/drivecred.json.

Demo:
cp ~/Downloads/drivecred.json ~
python3 gdrive10.py
"""

import os

print("os.environ['HOME']:")
print( os.environ['HOME'])

with open(os.environ['HOME'] + '/drivecred.json') as fh:
    drivecred_json_s = fh.read()

print(os.environ['HOME'] + '/drivecred.json' + ' has this JSON inside:')
print(drivecred_json_s)
