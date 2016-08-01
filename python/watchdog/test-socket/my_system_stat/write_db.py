#!/usr/bin/env python
#coding:utf-8

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler







class My_event_handler(FileSystemEventHandler):

    def __init__(self, fD):

        self.FILE_DATA = fD

    def on_modified(self, event):
        super(My_event_handler, self).on_modified(event)
        self.FILE_DATA.put(event.src_path+str(random.random()))



