lst = [1,2, 3, 4]

def yielding():
    yield from lst


val = yielding()
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
