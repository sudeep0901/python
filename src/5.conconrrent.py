
import os
import time
from concurrent.futures import ProcessPoolExecutor


def double(x):
    print(os.getpid())
    return x * 2


if __name__ == "__main__":
    print(os.getpid())
    values = [1, 2, 3, 4, 3]
    t0 = time.time()

    results = list(map(double, values))
    t1 = time.time()
    print(t1 - t0)
    executor = ProcessPoolExecutor()

    task = executor.submit(list(map(double, values)))
    print("I am main program")
    t2 = time.time()
    print(t2 - t1)
    
    task = executor.submit(list(map(double, values)))
    print(type(task.result))
    print(results)

