from gevent import monkey; monkey.patch_all()
import gevent
import psutil

from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin

from time import sleep
from os import popen

class SystemStatNamespace(BaseNamespace, BroadcastMixin):
    def recv_connect(self):
        def sendstat():
            while True:
                net_vals = psutil.net_io_counters()
                net_s_vals = net_vals.bytes_sent # sent bytes, total
                net_r_vals = net_vals.bytes_recv # recv bytes, total

                cpu_vals = psutil.cpu_percent(interval=1, percpu=True)
                cpu_vals = round(sum(cpu_vals)/len(cpu_vals), 1)

                mem_vals = psutil.virtual_memory()
                mem_vals = round(mem_vals.percent, 1)

                disk_vals = popen('iostat | grep sda').read().strip().split()
                disk_r_vals = disk_vals[2] # read, kb/s
                disk_w_vals = disk_vals[3] # write, kb/s

                net_vals = psutil.net_io_counters()
                net_s_vals = round((net_vals.bytes_sent - net_s_vals)/1024.0, 2) # sent bytes/s, speed
                net_r_vals = round((net_vals.bytes_recv - net_r_vals)/1024.0, 2) # recv bytes/s, speed

                self.emit('sys_data',
                          {
                          'cpu': cpu_vals,
                          'memory': mem_vals,
                          'disk_r': disk_r_vals,
                          'disk_w': disk_w_vals,
                          'net_s': net_s_vals,
                          'net_r': net_r_vals
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
