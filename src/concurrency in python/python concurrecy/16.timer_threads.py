# Because the args and kwargs values passed to the Thread constructor are saved in private variables, they are not easily accessed from a subclass. To pass arguments to a custom thread type, redefine the constructor to save the values in an instance attribute that can be seen in the subclass.
import threading
import logging

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s',)

class MyThreadWithArgs(threading.Thread):

    # def run(self):
    #     logging.debug('running' + "initializing thread")
    #     t = threading.currentThread()
    #     lcl = threading.local()
    #     lcl.initialize = "Hello i initialized constructor"

    #     return
    
    def __init__(self, group=None, target=None, name=None,args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name)    
        self.args = args
        self.kwargs = kwargs
        self._target = target
        return

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        self._target()
        return

def worker():
    print("target executing subclass")

for i in range(5):
    print(globals())
    print(locals())

    t = MyThreadWithArgs(target=worker,args=(i,), kwargs={'a':'A','b':'B'})
    t.start()

