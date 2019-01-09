
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

from datetime import datetime

def not_during_night(func):
    def wrapper():
        print(datetime.now(), datetime.now().hour)
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper

# So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how you apply a decorator to a function.


@not_during_night
def say_whee():
    print("do not run at night")

say_whee = not_during_night(say_whee)
say_whee();

say_whee()



# decorator with parameters

