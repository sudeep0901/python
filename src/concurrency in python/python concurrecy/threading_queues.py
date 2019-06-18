from threading import Thread
from queue import Queue

def producer(queue):
        for i in range(10):
                print(str(i))
                # item = make_an_item_available(i)
                item = i
                queue.put(str(item))
    
        # queue.put(str("exit"))

def consumer(queue):
    while True:
        item =  queue.get()
        if item == "exit":
                break
        # print("Received item in queue fro thread" + item)
        queue.task_done()
        


queue = Queue()
t1 = Thread(target=producer, args=(queue, ))
t2 = Thread(target=consumer, args=(queue, ))
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
import time
t1.join()
while True:
        print(t1.isAlive() , t1.isDaemon())
        print(t2.isAlive() , t2.isDaemon(), t2.getName())
        # t2.daemon =False
        time.sleep(2)
