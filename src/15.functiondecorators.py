
# # decorators Example
# def beutify(func):
#     print("I am adding wait.....")
#     func()



# enable_tracing = False
# if enable_tracing:
#     debug_log = open("debug.log","w")
# def trace(func):
#     if enable_tracing:
#         def callf(*args,**kwargs):
#             debug_log.write("Calling %s: %s, %s\n" %
#             (func.__name__, args, kwargs))
#             r = func(*args,**kwargs)
#             debug_log.write("%s returned %s\n" % (func.__name__, r))
#             return r
#         return callf
#     else:
#         return func

# @trace
# def adder(x, y):
#     return (x + y)

# result = beutify(adder(1, 10))
# print(result)


def mydecorator(func):
    def wrapper():
        print("I am wrapper")
        func()
        print(func.__globals__)
        print("Somehting more interesting")
    return wrapper


def say_hi():
    x = "dict"
    print("Hello Decorators")

print(say_hi)

say_hi = mydecorator(say_hi)

say_hi()
