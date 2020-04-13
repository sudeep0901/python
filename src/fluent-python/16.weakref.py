import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print("Gone with the wind")


ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
s2 = 'spam'
print(ender.alive)


a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
a_set = {2, 3, 4}
print(wref() is None)

print(a_set)
print(wref())
print(wref() is None)


