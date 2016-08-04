#!/usr/local/bin/python

import sys
import redis
from time import sleep

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

resLogs = '' # whole residual error logs

isUpdate = '' # res is updated or not

newRow = '' # a new resLogs row


class My_envent_handler(FileSystemEventHandler):

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def on_modified(self, event):
        super(My_envent_handler, self).on_modified(event)

        # self.r.set('isUpdate', True)
        self.r.rpush('resLogs', event.src_path)

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


