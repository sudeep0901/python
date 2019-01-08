a = 10
b = 20

#Localnamespace is created whn function is called and new objects are created
def scope1():
    a = 50
    b = 60
    print("Local Namespace: a, b" , a, b)

scope1()


def globalscope():
    global a 
    a = 900
    print("Global keywork makes global namespace in functions localnamespace:", a, b)

globalscope()
