# A memoryview is essentially a generalized NumPy array structure in Python itself
# (without the math). It allows you to share memory between data-structures (things like
# PIL images, SQLlite databases, NumPy arrays, etc.) without first copying. This is very
# important for large data sets.

from time import perf_counter as pc
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)
print(dir(numbers))
print(numbers.tobytes())

memv = memoryview(numbers)
print(len(memv))
for i in range(5):
    print(memv[i])

# Create memv_oct by casting the elements of memv to typecode 'B' (unsigned
    #  char).
memv_oct = memv.cast('B')
# memv_oct.to_list()
print(memv_oct[0])
print(memv_oct[1])
print(memv_oct[2])
print(memv_oct[3])

memv_oct[1] = 8
print(numbers)


random_byte_array = bytearray('ABC', 'utf-8')
print(random_byte_array)
print('Before updation:', random_byte_array)
mv = memoryview(random_byte_array)
mv[1] = 90
print('After updation:', random_byte_array)

t0 = pc()
for i in range(1000000000):
    pass

print(pc() - t0)
