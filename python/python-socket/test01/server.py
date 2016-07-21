import socket
import os, stat
import time

def fileIsChange(fileName):
    t=3
    size_0 = os.stat(fileName)[stat.ST_SIZE]
    time.sleep(t)
    size_1 = os.stat(fileName)[stat.ST_SIZE]
    if size_0 == size_1:
        return False
    else:
        return True

s = socket.socket()

host = socket.gethostname()
port = 8088

s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr

    # text_0 = []
    # isChange = True
    # while isChange:
    #     with open("example.out", "r") as f:
    #         text = f.read().split('\n')
    #         tmp = list(set(text).difference(set(text_0)))
    #         c.send('\n'.join(tmp))
    #     text_0 = text
    #     isChange = fileIsChange('example.out')


    data = c.recv(1024)

    if data:
        print "Data: {}".format(data)
        c.send(data)
        print "sent {} bytes back to {}".format(data, addr)
        with open("example.out", "r") as f:
            text = f.read()
        c.send(text)

    c.close()
