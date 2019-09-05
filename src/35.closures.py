def outer(mst):
    def inner():
        print("i am closure inner function")
        print(mst)
    return inner


another = outer("hello")
print(outer.__closure__)
# another

# del outer
# another()


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)

times3.__closure__
# print(make_multiplier_of.__closure__[0])

def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")

print(print_msg.__closure__)

def foo():
    def fii():
        pass
    return fii

f = foo()
f.func_closure
 