'''
Created on Dec 7, 2018

@author: Sudeep Patel


'''

from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(10)])

fib.cache_clear()

try:
    print([fib(n) for n in range(10)])
except:
    print("error occured")    

