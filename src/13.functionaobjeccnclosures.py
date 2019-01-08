import foo
from urllib.request import urlopen

variable = "sudeep"
variable1 = "sudeep"


def hellworld():
    print(hellworld.__globals__)
    return "Hello I am callsed using function pass"


 
def bar():
    x = 13
    print("running bar..")
    # print(bar.__globals__)

    def helloworld1():
        print(helloworld1.__globals__)

        return "Hello World. x is %d" % x
    print(foo.callf(helloworld1))  # returns 'Hello World, x is 13'
    print(helloworld1.__globals__)
    

# from urllib.request import urlopen (Python 3)
def page(url):
    def get():
        return urlopen(url).read()
    return get

# print(foo.callf(hellworld))
bar()

# python = page("http://www.python.org")
# print(python)
# print(python.__closure__)
# print(python())





# print(next.__globals__)
