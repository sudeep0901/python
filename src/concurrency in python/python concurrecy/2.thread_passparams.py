import threading
import time
def worker(num):
    print("worker" , num)
    time.sleep(2)
    return
threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for th in threads:
    print("waiting for threads to complete")
    th.join()

print("testing")