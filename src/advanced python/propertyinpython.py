class propertyclass:
    def __init__(self, value):
        self._value = value

    def getvalue(self):
        print("getting value")
        return self._value

    def setvalue(self, value):
        print("setting value")
        self._value =value


    def delvalue(self):
        print("Deletin value")
        del self._value


    value = property(getvalue, setvalue, delvalue)


pc = propertyclass("sudeep")

print(pc.value)
pc.value = 5000

print(pc.value)