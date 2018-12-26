from IPython.utils.py3compat import xrange
price = '200'

print(price.zfill(4))

name = "sudeeppatel"

print(name.upper())

print(name.swapcase())
print(name.swapcase())

print(name.isalnum(), name.isalpha(), name.isdigit())
name = "sudeep patel"

print(name.isalnum(), name.isalpha(), name.isdigit())

print(name.encode(encoding='utf_8', errors='strict'))
print((name.encode(encoding='utf_8', errors='strict')))

print(name.capitalize())
listofnnum = range(1, 6)
print(listofnnum)

for i in listofnnum:
    print(i)


st = set([1, 4, 5, 33])

fst = frozenset([1, 4, 5, 33])

print(st)
print(fst)

print(len(st), st.union(fst))