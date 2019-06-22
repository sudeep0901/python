import random
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s',)

def worker():
    print("running worker thread", threading.currentThread().getName())
    pause = random.randint(1, 5)
    print(pause)
    time.sleep(15)


for i in range(5):
    print("thread number:" , i)
    t = threading.Thread(name="worker:" + str(i), target=worker)
    t.start()
main_thread = threading.currentThread()

for t in threading.enumerate():
    if t is main_thread:
        continue
    
    print("Enumerated: ", t.getName())
    t.join()
