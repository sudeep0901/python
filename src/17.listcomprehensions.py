# List Comprehensions  - calling a function for list of values
#  A common operation involving functions is that of applying a function to all of the
# items of a list, creating a new list with the results.

import math

items = [1, 2, 3, 4, 5]

square = [n * n for n in items]
print(square)

#filter
square = [n * n for n in items if n > 3]
print(square)

names = ["sudeep", "Manasvi", "Mahesh", "Prabha",  "Renu"]
[print(name) for name in names]


def printname(name):
    print(name)
    name = "Hello, " + name
    return name


updatedValues = [printname(name) for name in names]
print(updatedValues)

a = [-3, 5, 2, -10, 7, 8]
b = 'abc'

# packing differnt lists
combined = [(a, b) for x in a
            for y in b]

print(combined, type(combined))


f = [(1,2), (3,4), (5,6)]
g = [math.sqrt(x*x+y*y) # f = [2.23606, 5.0, 7.81024]
for x,y in f]

print(g)