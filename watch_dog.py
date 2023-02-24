import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

import subprocess

class ReloadEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print('Рестартую Бота')
        subprocess.call(['bot_run.bat'], stdout=None)

if __name__ == "__main__":
    # subprocess.call(['bot_run.bat'])
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    # event_handler = FileSystemEventHandler()
    event_handler = ReloadEventHandler()
    # event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)

    finally:
        observer.stop()
        observer.join()