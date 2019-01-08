
# closure Example

def counter(n):
    def next():
        nonlocal n
        r = n
        n -= 1
        # print(next.__globals__)
        print(type(next.__globals__))
        for val in next.__globals__:
            print(type(val), val)

        return r
    return next

next = counter(10)

print(next())
# print(next.__globals__)

print(next())
print(next())

print(next())

print(next())