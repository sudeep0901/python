def print_name(prefix):
    print("Searching for prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)

# Execution of coroutine is similar to the generator. When we call coroutine nothing happens, it runs only in response to the next() and send() method. This can be seen clearly in above example, as only after calling __next__() method, out coroutine starts executing. After this call, execution advances to the first yield expression, now execution pauses and wait for value to be sent to corou object. When first value is sent to it, it checks for prefix and print name if prefix present. After printing name it goes through loop until it encounters name = (yield) expression again.
corou = print_name("dear")
corou.__next__() 
corou.send("Sudeep")
corou.send("dear Sudeep")
corou.close()


def add_values(val):
    while True:
        value1 = (yield)
        print(val + value1)


av = add_values(100)
av.__next__()
av.send(1000)
av.send(1001)
