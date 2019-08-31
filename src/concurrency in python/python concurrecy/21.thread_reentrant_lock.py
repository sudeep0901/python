import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

rlock = threading.RLock()

acquired = rlock.acquire()
print(acquired)

acquired = rlock.acquire()  # this blocks the main thread
print(acquired)

# this does not block main thread blocks the main thread
acquired = rlock.acquire(0)
print(acquired)
