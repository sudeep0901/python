import timeit
def test1():
    for i in range(10):
        i = i


def test():
    for i in range(10):
        print(i)
        yield i
    # return i

test_iter = test()
print(type(test_iter))
print(next(test_iter))
print(next(test_iter))
print(next(test_iter))

print(timeit.timeit(test1,number=100))


