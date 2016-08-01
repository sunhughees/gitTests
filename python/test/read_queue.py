from write_queue import que
import time


while True:
    if not que.empty():
        print que.get()
    else:
        print "nothing"
    time.sleep(3)



