# Signaling Between Threads¶
# Although the point of using multiple threads is to spin separate operations off to run concurrently, there are times when it is important to be able to synchronize the operations in two or more threads. A simple way to communicate between threads is using Event objects. An Event manages an internal flag that callers can either set() or clear(). Other threads can wait() for the flag to be set(), effectively blocking progress until allowed to continue.

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)


def wait_for_an_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug('wait_for_event starting')
    event_is_set =  e.wait()
    logging.debug("event set %s", event_is_set)
    process_file()

def process_file():
    logging.debug("Processing file as event is set")
    time.sleep(5)
    logging.debug("Processing finished")



def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    while not e.isSet():
        logging.debug('wait_for_event_timemout starting')
        event_is_set = e.wait(t)
        logging.debug("event is set: %s" , event_is_set)
        if event_is_set:
            logging.debug('processing event')
            logging.debug('processing file from internet')

        else:
            logging.debug('doing other work')


e = threading.Event()

e = threading.Event()
t1 = threading.Thread(name='block', 
                      target=wait_for_an_event,
                      args=(e,))


t1.start()

t2 = threading.Thread(name='non-block', 
                      target=wait_for_event_timeout, 
                      args=(e, 2,))

t2.start()
                      
logging.debug('Waiting before calling Event.set()')
time.sleep(5)
e.set()
logging.debug("Event is set")