a =  42

def test():
    print("testing objects")
    
# a.test = test()

# print(a, a.test())

print(id(a), id(a).__str__())

# check identifhy of the object


a =  40
b = a 
c = 40

def compare(a, b):
    if(a is b):
        print("Both objects are equal", id(a), id(b))
    else:
        print("Objects are not equal", id(a), id(b))
        
        
        
compare(a, b)
compare(a, c)

s = "Sudeep Patel"

# check type of instance
if (type(s) is list):
    print("List")
    
# Better way to check type of instance
if isinstance(s, str):
    print("Object is of type string")


# remove object referecne count
import sys

print(sys.getrefcount(a))
del a

# print(sys.getrefcount(a))


# circular dependancy

a = {}
b = {}

a['b'] = b
b['a'] = a

#However, because each object contains
# a reference to the other, the reference count doesnt drop to zero and the objects
# remain allocated (resulting in a memory leak).
# execution.The exact behavior can be fine-tuned and
# controlled using functions in the gc module
del a 
del b       


lsta = [10, 20, 30]
lstb = lsta

print(lsta is lstb)

lstb[2] =500

print(lsta, lstb) # both lists changed as lists are mutable


# To avoid this create a shallow Copy

al = [1, 2, [3, 4]]
bl = list(al) # creating shallow copy but copies object references
print(al is bl)


bl.append(6)
print(al)
print(bl)

bl[2][0] = 500
print(al)
print(bl)


#Deep copy

import copy
adl = [1, 2, 3, [4, 5]]
bdl= copy.deepcopy(adl)

bdl[3][0] =-100
print(adl, bdl)
