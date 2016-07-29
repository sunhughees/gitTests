import threading, time

def doWaiting1(event):
	print 'start waiting1:' + time.strftime('%H:%M:%S') + '\n'
	event.wait()
	time.sleep(0.1)
	print 'stop waiting1:' + time.strftime('%H:%M:%S') + '\n'

def doWaiting2(event):
	print 'start waiting2:' + time.strftime('%H:%M:%S') + '\n'
	event.wait()
	time.sleep(3)
	print 'stop waiting2:' + time.strftime('%H:%M:%S') + '\n'

# thread_1 = threading.Thread(target=doWaiting1)
# thread_1.start()
# thread_1.stop()

# thread_2 = threading.Thread(target=doWaiting2)
# thread_2.start()

e = threading.Event()

t1 = threading.Thread(name='t1', target=doWaiting1, args=(e,))
t1.start()

t2 = threading.Thread(name='t2', target=doWaiting2, args=(e,))
t2.start()

time.sleep(1)

e.set()