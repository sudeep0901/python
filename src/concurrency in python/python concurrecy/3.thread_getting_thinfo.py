import threading
import time


def worker():
    print(threading.currentThread().getName(), "Starting")
    time.sleep(2)
    print(threading.currentThread().getName(), "Ending")

    return

t = threading.Thread(target=worker)
t.start()

print("testing")
