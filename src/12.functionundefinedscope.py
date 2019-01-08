i = 0
def foo():
    i = i + 1 # UnboundLocalError: local variable 'i' referenced before assignment
    print(i)

foo() # i does not reference to global variable