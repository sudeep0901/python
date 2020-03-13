from operator import itemgetter
from inspect import signature
from functools import reduce
from operator import add
res = reduce(add, range(100))
print(res)
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted_fruits = sorted(fruits, key=lambda word: word[::-1])
print(sorted_fruits)

sorted_fruits = sorted(fruits, key=lambda ln: divmod(len(ln), 2))
print(sorted_fruits)

# function to gemerate html tags


def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""

    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        print(content)
        print(attr_str)
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


# tag('p', 'hello', id=33, cls='sidebar')


# my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
#  'src': 'sunset.jpg', 'cls': 'framed'}
# tag(**my_tag)
#


# keyword only arguments
def f(a, *, b):
    return a, b


# print(f(1, b=2))

# fn = f(10, b=10)

# sig = signature(f(10, b=10))
# print(sig)


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

print(city)
city = itemgetter(1, 0)

for ct in metro_data:
    print(city(ct))
