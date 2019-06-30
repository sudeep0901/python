# Synchronizing Threads
# In addition to using Events, another way of synchronizing threads is through using a Condition object
# Because the Condition uses a Lock, it can be tied to a shared resource. This allows threads to wait for the resource to be updated. In this example, the consumer() threads wait() for the Condition to be set before continuing. The producer() thread is responsible for setting the condition and notifying the other threads that they can continue.

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug("resource is available to consumer")

def otherwaiting(cond):
    logging.debug("start the processsing")
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug("i am starting as got the green")
        

def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        import time
        logging.debug("working on my task and once complete with notify others to start")
        time.sleep(10)
        cond.notifyAll()

# creating condition object
condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
c3 = threading.Thread(name='c2', target=otherwaiting, args=(condition,))

p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
c3.start()
time.sleep(2)

p.start()