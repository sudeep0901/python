import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
lock = threading.Lock()

acquired = lock.acquire()
print(acquired)

# acquired = lock.acquire() # this blocks the main thread
# print(acquired)

acquired = lock.acquire(0) # this does not block main thread blocks the main thread
print(acquired)
