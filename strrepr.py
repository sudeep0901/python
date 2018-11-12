class StrRepr:
    pass

    def __str__(self):
        return "This str method"

    def __repr__(self):
        return "Thisrepro method"

    def hello(self):
        return "Hello Evaluation method"


obj = StrRepr()

print(str(obj))
print(repr(obj))

print(eval(repr(obj)))
