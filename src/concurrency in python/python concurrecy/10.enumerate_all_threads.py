import random
import threading
import time
import logging
import sys
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def worker():
    """thread worker function"""
    print("Locals values to thread:", threading.local())
    lcl = threading.local()
    lcl.Name = "sudeep"
    print(lcl.Name)
    t = threading.currentThread()
    print(threading.currentThread().getName())
    pause = random.randint(1, 5)
    print(pause)
    logging.debug('sleeping %s', pause)
    time.sleep(pause)

for i in range(1, 3):
    t = threading.Thread(target=worker)
    print(threading.currentThread().getName())
    t.setDaemon =  True
    t.start()

main_thread = threading.currentThread()
for threadId, stack in sys._current_frames().items():
    print("thread id: ", threadId, stack)

print(main_thread.getName())
print("total active theads: " , threading.active_count())



for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('continue joining %s', t.getName())
    t.join()

