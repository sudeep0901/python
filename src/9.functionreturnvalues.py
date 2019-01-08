a = [1, 2, 3, 4, 5]

# Mutable object passed to function and contents changed by called function and cause of subtle errors in programming

def square(items):
    for i, val in enumerate(items):
        print(i, val)
        items[i] = val * val

square(a)
# print(square(a))
print(a)


