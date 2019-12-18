import sys
print(0b1111)
print(bin(15))
print(bin(~0b1111))
print(bin(-4))
v = 0b111100
print(v)

v1 = ~v
print(v1, bin(v1))
int(32).bit_length()
int(0xcafebabe).to_bytes(length=4, byteorder='little')
little_cafebabe = int(0xcafebabe).to_bytes(length=4, byteorder=sys.byteorder)

sys.byteorder

int.from_bytes(little_cafebabe, byteorder=sys.byteorder)

# hex(_)

# bytes literal

byte = b'this is python byte literal'

print(byte)
print(byte[1])
print(bytes(range(65, 65 + 26)))
print(bytes.fromhex('abcd'))
print(bytes(bytes.fromhex('abcd')), 'utf16')
