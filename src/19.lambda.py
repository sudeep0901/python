# Anonymous functions in the form of an expression can be created using the lambda
# statement:
# lambda args : expression

a = lambda x, y : x + y
r = a(10, 20)

print(r)

def adder(x, y):
    return x + y

adder.description = "Function is used to add 2 variables"
b = lambda x, y : adder(x, y)
print(b)

print(b(50, 100))
print(adder.__dict__)
print(adder.description)

# The primary use of lambda is in specifying short callback functions. For example, if
# you wanted to sort a list of names with case-insensitivity, you might write this:
# names.sort(key=lambda n: n.lower())
def flatten(lists):
    for s in lists:
        if isinstance(s,list):
            flatten(s)
        else:
            print(s)


items = [[1,2,3],[4,5,[5,6]],[7,8,9]]
flatten(items) # Prints 1 2 3 4 5 6 7 8 9