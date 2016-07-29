from gevent import monkey; monkey.patch_all()
import gevent
import psutil

from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin

from time import sleep
from os import popen

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SystemStatNamespace(BaseNamespace, BroadcastMixin, FileSystemEventHandler):

    self.
    
    def on_modified(self, event):
        super(My_envent_handler, self).on_modified(event)



    def recv_connect(self):
        def sendstat():
            while True:
                cpu_vals = psutil.cpu_percent(interval=1, percpu=True)
                cpu_vals = round(sum(cpu_vals)/len(cpu_vals), 1)

                self.emit('sys_data',
                          {
                          'cpu': cpu_vals,
                          })
                gevent.sleep(0.1)

        self.spawn(sendstat)

class Application(object):
    def __init__(self):
        self.buffer = []

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
            socketio_manage(environ, {'/sys_stat': SystemStatNamespace})

        else:
            return not_found(start_response)

def not_found(start_response):
    start_response('404 Not Found', [])
    return ['<h1>Not Found</h1>']

if __name__ == '__main__':

    import sys

    try:
        if sys.argv[1]:
            ip = str(sys.argv[1])
    except:
        ip = '0.0.0.0'
    try:
        if sys.argv[2]:
            port = int(sys.argv[2])
    except:
        port = 8080

    print 'Listening on port http://%s:%s' %(ip, str(port))

    SocketIOServer((ip, port), Application(),
        resource="socket.io", policy_server=True,
        policy_listener=('0.0.0.0', 10843)).serve_forever()
