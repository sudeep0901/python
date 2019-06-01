def outerfunct(x):
    def innterfunc():
        print(x)
    innterfunc()


def outerfunct1(x):
    def innterfunc():
        print(x)
    return innterfunc

outerfunct(10)

innerfunc = outerfunct1(100)
print(innerfunc, innerfunc())
innerfunc()
print(innerfunc.__dict__)