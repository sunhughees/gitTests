import time
import random


def writeLog(n):
	for i in xrange(n):
	    with open('hello-%s.txt' %str(i), 'a') as f:
	        f.write("Hello, %s \n" %str(i))
	    time.sleep(0.5*random.random()+0.1)

for i in range(10):
	writeLog(10)
