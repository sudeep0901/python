def sum1(n):
    final_sum = 0
    for x in range(n +1 ):
        final_sum += x
    
    return final_sum


sum1(5)

def sum2(n):
    return (n * (n + 1)) / 2
    
sum2(5)

import timeit

timeit.timeit('sum1(100)', setup="from __main__ import sum1" )
timeit.timeit('sum2(100)', setup="from __main__ import sum2" )

# memory space
# time to run
