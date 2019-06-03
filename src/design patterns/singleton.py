import sys

print(sys.version)

class Singleton(object):
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
    

assert s1 is s2

s1.ans = 42