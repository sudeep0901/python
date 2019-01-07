import sys
code_obj = compile('sum[1,2,3]', '<string>', 'exec')
print(code_obj)
print(code_obj.co_name)
print(code_obj.co_argcount)
print(code_obj.co_nlocals)
print(code_obj.co_varnames)

# exec(code_obj)       

# raise NameError
# from math import *
# exec("print(dir())")

try:
    exec(code_obj)
except TypeError as te:
#     print(sys.exc_info())
    var = sys.exc_info()
    print("printing var:....", var)
 
    


