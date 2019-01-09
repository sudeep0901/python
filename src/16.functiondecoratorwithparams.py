import functools
def adderdecorator(func):
    @functools.wraps(func) #so that origional function do not loose its identity
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        # func(*args, **kwargs) to fix the return value issue return the value from calling function
        return func(*args, **kwargs)
    return wrapper

@adderdecorator
def adder(x , y, fun="running adder for your values"):
    return x + y
print(adder.__name__) # output wrapper without functools.wraps, and with functool output is adder
result = adder(2 , 2)
print(result)
