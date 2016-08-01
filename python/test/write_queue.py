import Queue


que = Queue.Queue()

while True:
    x = raw_input("Please write something:\n")
    que.put(x)
    print "wrote %s" %x

    