"""
cr5inst.py

This script should use syntax in gcloud10.bash to create 5 GCE instances.

With my mouse, I should get a Bash syntax from this page:
https://console.cloud.google.com/compute/instancesAdd
Then, I should paste the string into a file:
gcloud10.bash

This Python script should then read that file 5 times and create 5 instances.

Demo:
python3 cr5inst.py
"""

import subprocess

# I should read gcloud10.bash into a string:
with open('gcloud10.bash') as fh:
    my_s = fh.read()

# I should create 5 scripts from names of states:
for instance_name_s in ['calif', 'tx', 'newyork', 'mass', 'colo']:
    ur_s     = my_s.replace('instance-2',instance_name_s).replace('gcloud10',instance_name_s)
    script_s = '/tmp/' + instance_name_s + '.bash' 
    with open(script_s, 'w') as fh:
        fh.write(ur_s)
    # I should run each script:
    subprocess.run(["/bin/bash", script_s])    
