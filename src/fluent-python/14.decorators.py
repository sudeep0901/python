import time
from dis import dis


def deco(func):
    def inner():
        print("running inner")
    return inner


@deco
def target():
    print(globals())
    print(locals())
    print("Running target()")


print(target)
print(target())

registry = []


def register(func):
    dbconn = "Db connections"
    print('running register %s' % func)
    registry.append(func)
    print(func.__dict__)
    func.dbconn = dbconn
    func.__dict__['dbconn'] = dbconn
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


@register
def f3():
    print('running f3()')


def main():
    print(registry)
    f1()
    print(f1.dbconn)
    f2()
    f3()


if __name__ == "__main__":
    main()

promos = []


def list_of_functions(func):
    promos.append(func)
    return func


@list_of_functions
def add(x):
    return x


@list_of_functions
def add1(x):
    return x


@list_of_functions
def add2(x):
    return x


res = ((f(2) for f in promos))
print(next(res))
print(next(res))
print(next(res))
# print(next(res))


b = 10


def printvar(a):
    print(a)
    global b
    print(b)
    # if global b not defined UnboundLocalError: local variable 'b' referenced before assignment
    b = 10


printvar(100)

print(dis(printvar))

# Implementing a Simple Decorator


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(100))
