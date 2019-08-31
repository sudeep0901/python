class propertyclass:
    def __init__(self, value, newvalue, doubleunderscore):
        self._value = value
        self._newvalue = newvalue
        self.__baz = doubleunderscore

    def getvalue(self):
        print("getting value")
        print(repr(self.__dict__))
        return self._value

    def setvalue(self, value):
        print("setting value")
        self._value = value

    def delvalue(self):
        print("Deletin value")
        del self._value
    value = property(getvalue, setvalue, delvalue)


pc = propertyclass("sudeep", "newvalues", "Double Underscore")

print(pc.value)
pc.value = 5000
pc._newvalue = 1000
print("New VAues:::", pc._newvalue)
print(pc.value)
print("getattr:", getattr(pc, "value"))
 