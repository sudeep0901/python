s = 'cafcafé'
print(len(s))

s_utf = s.encode('utf-8')
print(s_utf)

cafe = bytes(s, encoding='utf-8')
print(cafe[0])
print(cafe[::1])  # slices gives bytes of bytes

for i in cafe:
    print(i)

cafe_arr = bytearray(cafe)
print(cafe_arr)


# The first
# thing to know is that there are two basic built-in types for binary sequences: the immutable
# bytes type introduced in Python 3 and the mutable bytearray, added in


bfh = bytes.fromhex('32 4A CE A9')
print(bfh)
