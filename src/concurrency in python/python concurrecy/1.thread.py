import threading
import time
def worker():
    print("worker")
    time.sleep(2)
    return
threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for th in threads:
    print("waiting for threads to complete")
    th.join()

print("testing")