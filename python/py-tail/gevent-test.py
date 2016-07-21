# from gevent import monkey; monkey.patch_socket()

# import gevent

# def f(n):
# 	for i in range(n):
# 		print gevent.getcurrent(), i

# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)

# map(lambda x: x.join(), [g1, g2, g3])

#----------------------------------------------------------

# import os
# import stat
# import time

# print os.getcwd()

# st = os.stat("gevent-test.py")

# print st

# print time.ctime(st[stat.ST_ATIME])

# print st[stat.ST_SIZE]/1024.,"kb"

# print st[6]


# fh = open('gevent-test.py', 'r')

# print len(fh.read())

# fh.close()

# print 'hello {i}'.format(i='world')

#----------------------------------------------------------

import os

class ReadLine(object):

	def __init__(self):
		pass

	# @property
	# def foo(self):
	# 	return self._foo
	
	# @property
	def _procList(self):
		# self._procList = [_i for _i in os.listdir('/proc') if _i.isdigit()]
		# return self._procList
		return [_i for _i in os.listdir('/proc') if _i.isdigit()]

rf = ReadLine()

print rf._procList()
