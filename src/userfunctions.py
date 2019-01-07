def foo(x, y):
    return x + y

# lambda function


bar = lambda x, y : x + y
result = bar(2, 3)

print(result)

print(bar.__name__)
print(bar.__dict__)
print(bar.__code__)
print(foo.__defaults__)
print(foo.__globals__)

print(foo.__dir__)