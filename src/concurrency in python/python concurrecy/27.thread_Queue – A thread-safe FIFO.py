# The Queue module provides a FIFO implementation suitable for multi-threaded programming. 
# It can be used to pass messages or other data between producer and consumer threads safely. 
# Locking is handled for the caller, so it is simple to have as many threads as you want working with the same Queue instance. 
# A Queue’s size (number of elements) may be restricted to throttle memory usage or processing.

import queue
import time
import threading
import random
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


q = queue.Queue()
# for i in range(4):
#     q.put(i)

# while not q.empty():
#     import time
#     # time.sleep(2)
#     print(q.get())

def rcvDataQueue(q):
    while True:
        logging.debug("waiting for data trigger")
        print(q.get())


def sendDataQueue(q):
    while True:
        logging.debug("sending data")
        time.sleep(1)
        q.put(random.randint(1, 100))

sender = threading.Thread(target=sendDataQueue, args = (q,))
receiver = threading.Thread(target=rcvDataQueue, args = (q,))
sender.setDaemon =True
receiver.setDaemon =True
q.put(10)
sender.start()
receiver.start()