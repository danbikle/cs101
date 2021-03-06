#!/bin/bash

# workon_tkrs.bash

# This script should subscribe to tkrs from GCP Pub/Sub.

# After this script gets a tkr-string from Pub/Sub. it should "work-on" the tkr.

# Demo:
# bash workon_tkrs.bash

# Work-around GCP gsutil bug:
export BOTO_CONFIG=/dev/null

cd ~
python workon_tkrs.py

exit
