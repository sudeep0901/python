# generators
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        

# for i in fib():
#     print(i )

print( "hello World")

# coroutines
def grep(pattern):
    print("Searching for" , pattern)
    while(True):
        line = (yield)
        if pattern in line:
            print(line)
            

search = grep('coroutine')

print(search)

next(search)

search.send("Sudeep Patel")   
search.send("coroutine")   

search.close()

print(search)