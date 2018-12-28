# postion in calling function and called does not matter as long as names are specified 
def foo(w, x, y):
    print(w, x, y)
    w = "I a changed"

    
foo(x=2, y="y", w="I am keywork parameter")

x = 2
y = "y"
w = "I am keywork parameter"
foo(w, x, y)
print(w)

try:
    foo(w)
except TypeError as t:
    print(t)


def printcomma(comma=','):
    print(comma)


printcomma(comma="comma")


def make_table(data, **parm):
    print(parm, data)


items = ['div', 'span', 'header']

make_table(items, fgcolor="black", bgcolor="white", border=1,
borderstyle="grooved", cellpadding=10,
width=400,)
