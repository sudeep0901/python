import multiprocessing
import time
def worker():
    '''worker function'''
    print("worker")
    time.sleep(100)
    return

 
def worker1(i):
    '''worker function'''
    name = multiprocessing.current_process().name
    print("worker", str(i),name )
    time.sleep(100)
    return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()

    jobs = []
    for i in range(5):
        name = "workker" + str(i)
        p = multiprocessing.Process(name=name ,target=worker1, args=(i,))
        jobs.append(p)
        p.start()

    