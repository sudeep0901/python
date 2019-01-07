'''
Created on Dec 7, 2018

@author: _patels13
'''

import time


def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        print(line)
        if not line:
            time.sleep(0.1)
            continue
        yield line


# Example use
if __name__ == '__main__':
    logfile = open("access-log.log")
    print(logfile)
    for line in follow(logfile):
        print(line)
 
        
