# arr = range(1, 10)

for i in range(10):
    i = i
    # print(arr)


def read_arr():
    for elem in range(10):
        # print(elem)
        yield elem


# Creating generator
read_generator = read_arr()
print(read_generator)
print(next(read_generator))
print(next(read_generator))
print(next(read_generator))
print(next(read_generator))
print(next(read_generator))
print(next(read_generator))
print(next(read_generator))
print(next(read_generator))
print(next(read_generator))
