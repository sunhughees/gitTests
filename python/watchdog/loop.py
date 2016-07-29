import pyinotify

wm = pyinotify.WatchManager()

notifier = pyinotify.Notifier(wm)

wm.add_watch('log/', pyinotify.ALL_EVENTS)

notifier.loop()
