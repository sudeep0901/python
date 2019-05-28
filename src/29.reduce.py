lst = [1,2, 3, 4,5]
from functools import reduce
rdc = reduce((lambda x, y:x * y), lst)
print(rdc)
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)


from  collections.abc import Iterable

if isinstance((number_list, filter(lambda x: x < 0, number_list)), Iterable):
    print("Iterable")


name = "sudeep patel"

res = ""
for s in name:
    res = s + res

print(res)

for s in reversed(name):
    print(s)


print(s)

print("".join(reversed(name)))

print(sorted(name), list(name).sort())

print(globals(), locals())

for i in range(10):
    print(i)
    continue 
    print(i * 10)

print("existed loop")