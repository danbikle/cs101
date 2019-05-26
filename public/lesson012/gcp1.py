"""
gcp1.py

Demo:
gcloud init
pip3 install google-api-python-client
visit: https://console.cloud.google.com/apis/credentials/serviceaccountkey
Use it to create srvacct1.json
export GOOGLE_APPLICATION_CREDENTIALS="${HOME}/.ssh/srvacct1.json"
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
  
