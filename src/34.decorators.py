def first(msg):
    print(msg)

second = first
print(second("hellos"))
print(type(second))
print(dir(second))
print(second.__globals__, second.__code__, second.__qualname__)
second.__dict__["dynamic params"] = "function mutated"
print(second.__dict__)


def inc(x):
    return x + 1


def dec(x):
    return x + 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 3))
print(operate(dec, 3))
print(operate.__call__)


def make_pretty(func):
    def inner():
        print("I am decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

ordinary()

pretty = make_pretty(ordinary)
pretty()

@make_pretty
def ordinary1():
    print("I am ordinary")

ordinary1()


def smart_divte(func):
    def inner(a, b):
        print("I am going to divide", a , b)
        if b == 0:
            print("cannot divide by zero")
            return
        return func(a, b)
    return inner


@smart_divte
def divide(a, b):
    return a / b


divide(1, 0)
print(divide(1, 11))

