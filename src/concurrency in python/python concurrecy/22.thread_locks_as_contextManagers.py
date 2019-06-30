import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def worker_with(lock):
    with lock:
        logging.debug("lock acquired")

def worker_nowith_lock(lock):
    try:
        lock.acquire()
    except:
        logging.debug("already locked")
    finally:
        logging.debug("lock released") 

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()