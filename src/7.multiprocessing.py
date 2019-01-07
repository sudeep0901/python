import multiprocessing
import time
 
def clock(interval):
    while True:
        print("the time is %s" % time.ctime())
        time.sleep(interval)
        

class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval
    
    def run(self):
        while True:
            print("The time is %s" % time.ctime())
            time.sleep(self.interval)
# if __name__ == '__main__':
# p = ClockProcess(15)
# p.start()
 
if __name__ =='__main__':
    p = multiprocessing.Process(target=clock, args=(15,))
    print("starting processing. . . . . .:")
    p.start()
    