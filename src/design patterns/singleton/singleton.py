import sys

print(sys.version)
class NoAttributesClassMeta(type):
    def __setattr__(cls, name, value):
        if name not in cls.__dict__:
            print(cls.__class__.__class__)
            raise AttributeError("Cannot set attributes")
        type.__setattr__(cls, name, value)

# violates SRP signle responsinilty principle
# NON STATNDARD Clas
# hard to test
# carry global state 
# signleton also called as antipattern
class Singleton(metaclass=NoAttributesClassMeta):
    ans = None
     
    @staticmethod
    def instance():
        if "_instance" not in Singleton.__dict__:
            Singleton._instance = Singleton
        return Singleton._instance


s1 = Singleton.instance()
s2 = Singleton.instance()
if (s1 == s2):
    print("Signleton", id(s1), id(s2), s1._instance())

try:
    s1.myobject = "test"
    print(s1.myobject)
    print(s1.__dict__)

except AttributeError:
    "cannot set new object on Signleton"

assert s1 is s2

s1.ans = 42