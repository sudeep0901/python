lfunc= lambda x : x + 1
print(lfunc(100))

# Immediately Invoked Function Expression
(lambda x, y: x + y)(2, 3)
print((lambda x: x*x)(2))

import dis

add = lambda x: x**x 
dis.dis(add)

(lambda x: (x % 2 and 'odd' or 'even'))(3)
(lambda x: (x % 2 and 'odd' or 'even'))(3)

def full_name(first: str, last: str) -> str:
    return f'{first.title()} {last.title()}'


full_name("sudeep", "patel")
(lambda x, y, z=3: x + y + z)(1, 2)

(lambda *args: sum(args))(1,2,3)
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)

def key_args(**kwargs):
    print(kwargs.values())
    print(kwargs.keys())
    print(len(kwargs))

key_args(a=1, b=2)