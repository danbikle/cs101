"""
gcp2.py

Demo:
pip3 install google-api-python-client
export GOOGLE_APPLICATION_CREDENTIALS=$HOME/secret.json
cat   $GOOGLE_APPLICATION_CREDENTIALS
python3 gcp2.py
"""

import googleapiclient.discovery
compute   = googleapiclient.discovery.build('compute', 'v1')
project_s = 'shining-sol-241621'
name_s    = 'linuxbox5'
zone_s    = 'us-central1-a'
machine_type_s = "zones/"+zone_s+"/machineTypes/n1-standard-1"

# Get the latest Debian Jessie image.
image_response = compute.images().getFromFamily(
    project='debian-cloud', family='debian-9').execute()
source_disk_image = image_response['selfLink']

config = {
    'name':        name_s,
    'machineType': machine_type_s,
    # Specify the boot disk and the image to use as a source.
    'disks': [
        {
            'boot': True,
            'autoDelete': True,
            'initializeParams': {
                'sourceImage': source_disk_image,
            }
        }
    ],
    # Specify a network interface with NAT to access the public
    # internet.
    'networkInterfaces': [{
        'network': 'global/networks/default',
        'accessConfigs': [
            {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
        ]
    }]
}

compute.instances().insert(project=project_s, zone=zone_s, body=config).execute()

print(source_disk_image)
print(project_s)
print(zone_s)
print(config)
