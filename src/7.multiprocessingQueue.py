import multiprocessing
import time
 

def consumer(input_q):
    while True:
        item = input_q.get()
        # Process Item
        if item is None:
            break
        print(item)  # replace with userful work
        input_q.task_done()
    # Shutdown
    print("Consumer done")


def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)
        print(item, "sent to queue", output_q)
        time.sleep(10)
        

if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()
    
    prod_p = multiprocessing.Process(target=producer, args=(q,))
    sequence = [1, 2, 3, 4]
    
    producer(sequence, q)
    
#     q.join()
 
