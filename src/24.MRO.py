class A():
    def sd(self):
        print("I am in class A")
        print(self.__dict__)


class B():
    def sd(self):
        print("I am in class B")
        print(self.__class__)


class C(A):
    def sd(self):
        print("In class C")


class D(B, C):
    pass


b = B()

b.sd()

d = D()
d.sd()

print(D.__mro__)
