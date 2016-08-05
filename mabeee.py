#!/usr/bin/python

import sys
import requests
import json

baseurl = 'http://localhost:11111'

path = '/'
if (2 == len(sys.argv)):
    path = sys.argv[1]

url = baseurl + path
print url

response = requests.get(url)

print response.status_code
if (0 < len(response.content)):
    print json.dumps(json.loads(response.content), indent=4, sort_keys=True)
