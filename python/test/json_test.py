#!/usr/bin/env python

import json

a = range(10)

b = json.dumps(a)

print type(b)

c = json.loads(b)

print a==c

# help(json)

# print json.dumps({'a':1})
