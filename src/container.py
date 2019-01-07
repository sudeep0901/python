a = [1, "a"]

print(list)
print(dir(list))

list = [1, "a"]
print(dir(list))

tuple = ("a", "b")
print(list)
print(tuple)

dictn = {"key": "dictionary",
         "d" :a}

print(dictn)


def factorial(n):
    "Factorial calculation string document string"
#     print("Calculating factorial of ", n)
    if n <= 1: return 1
    else: return n * factorial(n - 1)

    
print(factorial(100))
# printing document string
print(factorial.__doc__)

