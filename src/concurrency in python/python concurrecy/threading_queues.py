from threading import Thread
from queue import Queue

def producer(queue):
    for i in range(10):
        print(str(i))
        # item = make_an_item_available(i)
        item = i
        queue.put(str(item))

def consumer(queue):
    while True:
        item =  queue.get()
        print("Received item in queue fro thread" + item)
        queue.task_done()


queue = Queue()
t1 = Thread(target=producer, args=(queue, ))
t2 = Thread(target=consumer, args=(queue, ))

t1.start()
t2.start()
