from collections import namedtuple
import os
lax_coordinates = (33.9425, -118.408056)

city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s / %s' % passport)


# The for loop knows how to retrieve the items of a tuple separately—this is called
# “unpacking.” Here we are not interested in the second item, so it’s assigned to
# _, a dummy variable.
for city, _ in sorted(traveler_ids):
    print(city)


# Extended Iterable Unpacking

a, *b, c = range(5)

print(a, b, c)

print(*range(10))

# swapping
b, a = a, b

a, b = divmod(20, 5)
print(a, b)

t = (20, 8)
divmod(*t)
quotient, remainder = divmod(*t)
print(quotient, remainder)

print(os.getcwd())
_, filename = os.path.split(os.getcwd())
print(filename)
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)


def testfunc(x: int):
    print(x)


testfunc(10)

print(City._fields)

print(tokyo._asdict())

for ke, vl in tokyo._asdict().items():
    print(ke, vl)

print(tokyo.count(tokyo))


name = "Sudeep Mahesh chandra patel"
firstname = slice(0, 6)
print(name[firstname])

