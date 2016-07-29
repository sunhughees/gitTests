#/usr/bin/env python

import time

for i in xrange(10):
    with open('hello-%s.txt' %str(i), 'a') as f:
        f.write("Hello, %s \n" %str(i))
    time.sleep(0.000001)
