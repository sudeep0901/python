a = 10

print(id(a))


def showvar(X=a):  # Default argument will not change
    print(X, id(X))
    

a = 20
print(id(a))
showvar()


def foo(x, items=[]):
    items.append(x)
    return items

    
print(foo(1))
print(foo(2))
print(foo(3))
print(foo(4))


def foo1(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

    
print(foo1(1))
print(foo1(2))
print(foo1(3))
print(foo1(4))

# receiving arbitrary number of arguments


def recvParams(*args):
    print(len(args))
    for i in args:
        print(i)


recvParams('a', 'b' , '1')

def fprintf(file, fmt, *args):
    file.write(fmt % args)
# Use fprintf. args gets (42,"hello world", 3.45)
# fprintf(out,"%d %s %f", 42, "hello world", 3.45)
