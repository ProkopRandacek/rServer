import json
from collections import namedtuple

c = json.loads(open("conf.json").read(), object_hook=lambda d: namedtuple("X", d.keys())(*d.values()))
