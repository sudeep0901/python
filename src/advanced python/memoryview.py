from memory_profiler import profile

byte_array = bytearray("XYZ", "utf-8")
print("Before update:", byte_array)

mem_view = memoryview(byte_array)
print(type(mem_view))
mem_view[2] = 74
print("After update:", byte_array)


@profile
def read_random():
    ba = bytearray(1024)
    ba1 = bytearray("\xab4 sudeeppatel 12434 &","utf-8")
    with open("/dev/urandom", "rb") as source:
        print(type(source))
        content = source.read(1024 * 10000)
        source.readinto(ba)
        # ba  =str(ba).encode('utf-8').strip()
        # print(str(ba)/.encode('utf-8').strip())
        # print(ba.decode('utf-8').strip())
        # for c in ba:
        #     print(chr(c), int(c))
        # print("".join(map(chr,ba)))
        print(ba1, "".join(map(chr, ba1)))


        # content_to_write = content[1024:]
        content_to_write = memoryview(content)[1024:]
    print("Content length: %d, content to write length %d" %
          (len(content), len(content_to_write)))
    # print(str(content_to_write))
    # i = 0
    # import time
    # with open("/dev/null", "wb") as target:
    #     target.write(content_to_write)
    #     for i in range(1024):
    #             print(bytes(content_to_write[i]), i)
    #             time.sleep(3)


if __name__ == '__main__':
    read_random()
    s = b"abcdefgh"
    view = memoryview(s)
    # print(view[1], bytes(view[1]))
    limited = view[1:3]
    print(bytes(view[1:]))