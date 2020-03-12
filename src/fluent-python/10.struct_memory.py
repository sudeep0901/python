import struct
fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

print(img)
header = img[:10]
print(header)
print(bytes(header))
unpacked_image = struct.unpack(fmt, header)
print(unpacked_image)
