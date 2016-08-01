from gevent import monkey; monkey.patch_all()
import gevent
import psutil

from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin

from time import sleep
from os import popen
import random


class SystemStatNamespace(BaseNamespace, BroadcastMixin):

    def __init__(self, fD):

        self.FILE_DATA = fD

    def recv_connect(self):
        def sendstat():
            while True:
                # cpu_vals = psutil.cpu_percent(interval=1, percpu=True)
                # cpu_vals = round(sum(cpu_vals)/len(cpu_vals), 1)

                # cpu_vals = random.random()
                if self.FILE_DATA.empty():                    
                    cpu_vals = 'Default'
                else:
                    cpu_vals = self.FILE_DATA.get()

                self.emit('sys_data',
                          {
                          'cpu': cpu_vals,
                          })
                gevent.sleep(0.1)

        self.spawn(sendstat)

class Application(object):
    def __init__(self, fD):
        self.buffer = []
        self.FILE_DATA = fD

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].strip('/') or 'index.html'

        if path.startswith('static/') or path == 'index.html':
            try:
                data = open(path).read()
            except Exception:
                return not_found(start_response)

            if path.endswith(".js"):
                content_type = "text/javascript"
            elif path.endswith(".css"):
                content_type = "text/css"
            elif path.endswith(".swf"):
                content_type = "application/x-shockwave-flash"
            else:
                content_type = "text/html"

            start_response('200 OK', [('Content-Type', content_type)])
            return [data]

        if path.startswith("socket.io"):
            socketio_manage(environ, {'/sys_stat': SystemStatNamespace(self.FILE_DATA)})

        else:
            return not_found(start_response)

def not_found(start_response):
    start_response('404 Not Found', [])
    return ['<h1>Not Found</h1>']

if __name__ == '__main__':

    import sys
    # import threading

    import multiprocessing

    # try:
    #     if sys.argv[1]:
    #         ip = str(sys.argv[1])
    # except:
    #     ip = '0.0.0.0'
    # try:
    #     if sys.argv[2]:
    #         port = int(sys.argv[2])
    # except:
    #     port = 8080


    import Queue

    file_data = Queue.Queue()

    def monitor_file():

        path = sys.argv[1] if len(sys.argv) > 1 else '.'

        event_handler = My_event_handler(file_data)

        observer = Observer()

        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        observer.join()

        # event.wait()

        # observer.stop()

        


    # if ctrl+c, stop monitor

    # try:
    #     while True:
    #         sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    # observer.join()



    # start socket.io server

    def socket_server():
    
        ip = '0.0.0.0'
        port = 8080

        print 'Listening on port http://%s:%s' %(ip, str(port))

        SocketIOServer((ip, port), Application(file_data),
            resource="socket.io", policy_server=True,
            policy_listener=('0.0.0.0', 10843)).serve_forever()

        # event.wait()

        # sys.exit()

    # e = threading.Event()

    # t1 = threading.Thread(name='t1', target=socket_server, args=(e,))
    # t1 = threading.Thread(target=monitor_file)
    t1 = multiprocessing.Process(target=monitor_file)
    t1.start()

    # t2 = threading.Thread(name='t2', target=monitor_file, args=(e,))
    # t2 = threading.Thread(target=socket_server)
    t2 = multiprocessing.Process(target=socket_server)
    t2.start()

    # try:
    #     while True:
    #         sleep(1)
    # except KeyboardInterrupt:
    #     e.set()





