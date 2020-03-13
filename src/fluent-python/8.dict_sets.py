# import builtins
from types import MappingProxyType
import argparse
import os
import collections.abc as abc
import collections
from collections import ChainMap
import builtins
mydict = {}
tup = ('a',)

print(isinstance(mydict, abc.Mapping))
print(isinstance(mydict, abc.MutableMapping))

print(isinstance(tup, abc.Mapping))
print(isinstance(tup, abc.MutableMapping))

# What Is Hashable?
# An object is hashable if it has a hash value which never changes during its lifetime (it
# needs a __hash__() method), and can be compared to other objects (it needs an
# __eq__() method). Hashable objects which compare equal must have the same hash
# value. […]

# The atomic immutable types(str, bytes, numeric types) are all hashable. A frozen
# set is always hashable, because its elements must be hashable by definition. A tuple is
# hashable only if all its items are hashable
tl = (1, 2, [30, 40])
# hash(tl) # error
tt = (1, 2, (23, 4, 4))
print(hash(tt))
print(tt.__hash__())
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)
print(a)
print(b)
print(c)
print(d)
print(e)

# print(hash(a))

index = collections.defaultdict(list)
index['A'].append('INDIA')
print(index)


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup)
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(ChainMap(baseline, adjustments)))
mp = dict(ChainMap(baseline, adjustments))
print(mp)


defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}
print(command_line_args)
# combined = ChainMap(command_line_args, os.environ, defaults)
combined = ChainMap(command_line_args, defaults)

print(combined)
print(combined['color'])
print(combined['user'])


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


d = {1: 'A'}
d_proxy = MappingProxyType(d)

print(d_proxy)

# d_proxy[2] = 'X'  # set item assignment not supported
d[2] ='B'
print(d_proxy)
