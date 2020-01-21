# type hinting new feture for editors 
# but still it is dynamic at runtime
def add_numbers(a: int, b: int) -> int:
    return a + b


print(add_numbers(5, 5))

# strings - python2 on ASCII python 3 unicode
print("hello".capitalize())
print("hello".replace('e', 'a'))
print("hello".isalpha())
print("hello".isdigit())
print("some, csv, data".split(','))

python_bool = True

print(int(python_bool))
print(str(python_bool))

none_var = None

# print(None + python_bool)  # error unsupported type
number = 0

if not number:
    print(number, "Falsy")

number = 10
if number:
    print(number, "Truthy")

a = 1
b = 2

# short form of if else ternary
"Bigger" if a > b else "Shorter"

friend_list = []

friend_list.append("Sudeep")
print(friend_list)
print('sudeep' in friend_list)
print(len(friend_list))

dict = {'name': "Sudeep", "age": 34, 'child': {'name': "Sudeep", "age": 34}}

print(dict)
dict["last_name"] = "Kowalski"

dict.get("name", "unknown")
dict.get("name1", "unknown")
dict.keys()
dict.values()

# Exception
dict.get("name1")
try:
    # dict[0]
    last_name = dict["last_name"]
    print(last_name, '\n', dict)
    numbered = 3 + last_name
except KeyError:
    print("Error in finding name")
except TypeError as error:
    print("Incorrect Operation", error)
# traceback for line numbers
# Generic expection
# generic exception handling
except Exception as e:
    print("Erros ocurred Unknown", e)

print("code executess")


x = b"Bytes objects are immutable sequences of single bytes"
print(x)


# triple single or double quotes allows multiple lines
x = b'''Python Tutorial,
Javascript Tutorial,
MySQL Tutorial'''
print(x)

x = b'El ni\xc3\xb1o come camar\xc3\xb3n'
print(x.decode())

# create a string with hexadecimal data
x = '45678c6c56f205876f72c64'
print(x)

# this class method returns a bytes object, decoding the given string object.
# the string must contain two hexadecimal digits per byte.
x = 'c6c56f205876f72c64'
y = bytes.fromhex(x)

y = [70, 111, 106, 94, 101, 100, 22, 95, 105, 22, 91, 87, 125, 135]
print(bytes(y))


# bytearray objects are a mutable counterpart to bytes objects
x = bytearray("Python bytearray", "utf8")
print(x)
