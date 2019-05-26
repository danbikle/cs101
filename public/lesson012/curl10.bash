#!/bin/bash

# curl10.bash

# works:
#curl -X POST -d @hello.json localhost:3101/home/takepost?sf=isin_CA

# I should remove line 1 from cr1inst.json:
sed 1d cr1inst.json > /tmp/cr1inst.json

# I should get line 1 from cr1inst.json, then cutout string: "POST ".
the_url=`sed -n 1p cr1inst.json|sed 's/POST //'`

set -x
/usr/bin/curl -X POST -d @/tmp/cr1inst.json ${the_url}?"API_KEY=$API_KEY" 

exit
