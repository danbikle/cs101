"""
gcp1.py

Demo:
sudo apt install python3-pip
sudo pip3 install google-api-python-client
visit: https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts
Use it to create secret.json
export GOOGLE_APPLICATION_CREDENTIALS="${HOME}/secret.json"
python3 gcp1.py
"""

import googleapiclient.discovery
compute   = googleapiclient.discovery.build('compute', 'v1')
project_s = 'shining-sol-241621'
zone_s    = 'us-central1-a'

result = compute.instances().list(project=project_s, zone=zone_s).execute()

if 'items' in result:
  items_l = result['items']
  item0   = items_l[0]
  print(item0['status'])
  print(item0['machineType'])
  print(item0['cpuPlatform'])
  print(item0['networkInterfaces'][0]['accessConfigs'])
  
