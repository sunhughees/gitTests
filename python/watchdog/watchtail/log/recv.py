import redis
from time import sleep

r = redis.StrictRedis(host='localhost', port=6379, db=0)


n = 0
while True:

	if r.exists('isUpdate') and eval(r.get('isUpdate')):
		print r.get('isUpdate')
		# print "yes\n"
		r.set('isUpdate', False)
		n += 1
		print n
	else:
		# print "no\n", n
		sleep(0.02)
	# print "--*"*20+"--"
	# sleep(0.2)
