import http.client
from urllib.request import urlopen
import warnings
import os
import json
import logging
from os import path

logging.basicConfig(level=logging.DEBUG)
http.client.HTTPConnection.debuglevel = 1
URL = 'http://www.oreilly.com/pub/sc/osconfeed'

print(os.path.dirname(__file__))

curdir = os.path.dirname(__file__)
JSON = curdir + '/data/osconfeed.json'

def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


feed = load()
sort_sch = sorted(feed['Schedule'].keys())
print(sort_sch)
for key, value in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(value), key))

