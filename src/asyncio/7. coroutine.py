def print_name(prefix):
    print("searchingname with" + prefix)
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit as identifier:
        print("Coroutine Exited")


corou = print_name("Dear")

corou.__next__()

corou.send("Atul")
corou.send("Dear Atul")
corou.close()