#/usr/bin/env python
# -*- coding: utf-8 -*-
# import libs for socket.io
from gevent import monkey; monkey.patch_all()
import gevent
import psutil

from socketio import socketio_manage
from socketio.server import SocketIOServer
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin

from time import sleep
from os import popen

# import libs for watchdog

import sys
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class My_envent_handler(FileSystemEventHandler):
    """Write all the events captured."""

    def on_moved(self, event):
        super(My_envent_handler, self).on_moved(event)

        what = 'directory' if event.is_directory else 'file'
        with open('log.txt', 'a') as f:
            f.writelines("Moved %s: from %s to %s\n" %(what, event.src_path,
                     event.dest_path))

    def on_created(self, event):
        super(My_envent_handler, self).on_created(event)

        what = 'directory' if event.is_directory else 'file'
        with open('log.txt', 'a') as f:
            f.writelines("Created %s: %s\n" %(what, event.src_path))

    def on_deleted(self, event):
        super(My_envent_handler, self).on_deleted(event)

        what = 'directory' if event.is_directory else 'file'
        with open('log.txt', 'a') as f:
            f.writelines("Deleted %s: %s\n" %(what, event.src_path))

    def on_modified(self, event):
        super(My_envent_handler, self).on_modified(event)

        with open(event.src_path, 'r') as f:
            last_line = f.read().strip().split('\n')[-1]

        print last_line

        with open('new.log', 'a') as f:
            f.writelines(last_line+'\n')

        what = 'directory' if event.is_directory else 'file'
        with open('log.txt', 'a') as f:
            f.writelines("Modified %s: %s\n" %(what, event.src_path))


if __name__ == "__main__":

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = My_envent_handler()
    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
