"""
post1inst.py

This script should use the REST API to create a GCE instance.

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
line1_s    = matches.group(0)
post_url_s = matches.group(2)
post_url_s = 'https://httpbin.org/post'
post_url_s = 'http://localhost:3101/home/takepost'
json_s     = jsonf_s.replace(line1_s,'')
# I should POST my JSON to the URL listed in line 1 of the JSON file:
req = requests.post(post_url_s, json=json_s)
