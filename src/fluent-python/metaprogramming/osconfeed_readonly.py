import logging
from osconfeed import load
from frozenjson import *
from frozenattr import *
logging.basicConfig(level=logging.DEBUG)

raw_feed = load()
feed = FrozenJSON(raw_feed)

print(len(feed.Schedule.keys()))
for key, value in sorted(feed.Schedule.items()):
    print('{:3} {}'.format(len(value), key))


sudeepFrozen = FrozenAttr(raw_feed)
print(sudeepFrozen)
print(len(sudeepFrozen.Schedule))
for key, value in sudeepFrozen.Schedule.items():
    print(key, value)