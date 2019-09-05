import re

pattern = '^a...s$'
test_String = 'abyss'
result = re.match(pattern, test_String)
# print(result)

pattern = '[^sdp ]'
test_String = 'sudeep aptel'
result = re.match(pattern, test_String)
if result:
    print("matched")


pattern = '[0-9]'

test_String = '12334a '
result = re.match(pattern, test_String)
if result:
    print("matched 0-0")
pattern = 'm$'
test_String = 'sudeep  112 patel.com'

result = re.match(pattern, test_String)
if result:
    print("matched com")

pattern = '\d'
test_String = 'all12chars'
result = re.match(pattern, test_String)
if result:
    print("mixed numbers ")
else:
    print("all chars")

pattern = '\w'
test_String = 'Python'
result = re.match(pattern, test_String)
if result:
    print("space found  ")
else:
    print("no space foun")

# Program to extract numbers from a string

test_string = 'hello 12 hi 89. Howdy 34'
pattern = '^\d+'
result = re.findall(pattern, test_string)
print(result)
test_string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, test_string, 1)
print(result)

# Program to remove all whitespaces
# multiline string
test_string = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'

replace = '---'

new_string = re.sub(pattern, replace, test_string, 2)
print(new_string)

new_string = re.subn(pattern, replace, test_string)
print(new_string[0], new_string[1])

string = "Python is fun"
# check if 'Python' is at the beginning
result = re.search('\APython', string)
print(result)
print(dir(result))
print(result.group())