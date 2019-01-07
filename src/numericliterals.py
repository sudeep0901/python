print(True)

if (True == 1): # boolean is equal to integer 0 / 1
    print("equal")
else:
    print("Unequal")

val = 1234

print(1234)
print(type(1234), type(val))

# Binary
print(0b1111)

# Octal 
print(0o007)

# Hexadecimal
print(0x007)

print('Hello i am string \\n literal \v vertical tab')

print("Hello i am string literal")

# Multiline printing
print("""Hello i am string literal
I am 
multiple 
print 
statement""")

# \x to print special characters
print("Jalape\xf1o")

s = u"Jalape\u00f1o"

print(s, type(s))

print(u"\u002f1")

# raw text

print(r"\Hello# $\ns")

print("raw path:", r'c:\newdata\tests')

print('Jalape\xc3\xb1o', b'Jalape\xc3\xb1o')