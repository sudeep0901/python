ini_dict = {"a": 1, "b":2, "c":3,"b":2, "d":0}
print(ini_dict)

flipped = {}

for key, value in ini_dict.items():
    if value not in flipped:
            flipped[value] = [key]
    else:
        flipped[value].append(key)

print(str(flipped))

rev_dict = {}

for key, value in ini_dict.items():
    rev_dict.setdefault(value, set()).add(key)

print(str(rev_dict))

from itertools import chain
result = set(chain.from_iterable( 
         values for key, values in rev_dict.items() 
         if len(values) > 1)) 

print(result, str(result))

import operator

sorted_X = sorted(ini_dict.items(), key=operator.itemgetter(0))
print(sorted_X)

for val in sorted_X:
    print(val)

import collections

sorted_dict =  collections.OrderedDict(ini_dict)
print(sorted_dict)
