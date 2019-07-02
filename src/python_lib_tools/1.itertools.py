from itertools import *

for i in chain([1, 2, 3], ['A', 'B', 'C']):
    print(i)

ls = [1, 2,3, 4]
iterat = chain(ls)
print(type(iterat))