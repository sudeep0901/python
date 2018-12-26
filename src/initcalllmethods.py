class Foo:

    def __init__(self, a , b , c):
        self.a = a
        self.b = b
        self.c = c
        print(a, b, c)
    
    def __call__(self, a , b, c):
        self.a = a
        self.b = b
        self.c = c
        print(a, b, c)

def printHello(self):
        print("Hey i am add function to an instance dynamically")
        
x = Foo(1 , 2, 3)  # invokes __init__

# x.printHello = printHello(x)

print(type(Foo), type(x), x.__class__)

#instance Data
print(x.__dict__)

# Defining a custom __call__() method in the meta-class allows the class's instance to be called as a function, not always modifying the instance itself.
x(11, 22, 33)  # invokes __call__ method

x.a = 0

print(x)

print(x.a, x.b, x.c)

#  y = Foo.__call__(y, 99, 88 , 77)

# print(y.a, y.b, y.c)
