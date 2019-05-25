"""
post1inst.py

This script should use the REST API to create a GCE instance.

With my mouse, I should get a JSON string from this page:
https://console.cloud.google.com/compute/instancesAdd
Then, I should paste the string into a file:
cr1inst.json

With my mouse, I should get an API_KEY from this page:
https://console.cloud.google.com/apis/credentials
Then, I should paste the string into a file:
api_key.txt

Then, this Python script should have a hope.

Demo:
python3 post1inst.py
"""

import re
import requests

# I should load the JSON file into a string:
with open('cr1inst.json') as fh:
  jsonf_s = fh.read()

# I should use a regexp to get the POST-URL:
matches    = re.search('(POST )(https.*instances)', jsonf_s)
line1_s    = matches.group(0) # s.b. Useful later
post_url_s = matches.group(2)
print('I will POST a request to this URL:')
print(post_url_s)

# I should get the API_KEY string from api_key.txt
# which I got from this URL:
# https://console.cloud.google.com/apis/credentials

with open('api_key.txt') as fh:
  api_key_s = fh.read()

params_d   = {'key': api_key_s}
# post_url_s = 'http://localhost:3101/home/takepost'
json_s     = jsonf_s.replace(line1_s,'')
# json_s     = '{"hello": "world"}' # for now
# I should POST my JSON to the URL listed in line 1 of the JSON file:
req = requests.post(post_url_s, params=params_d, json=json_s)
print('Done')
