import os
from  concurrent.futures import ProcessPoolExecutor

def task():
    print("Executing out Task on Processs: {}".format(os.getpid()))

def main():
    # executor = ProcessPoolExecutor()
    with ProcessPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task)
        task2 = executor.submit(task)

if __name__ == '__main__':
    main()
