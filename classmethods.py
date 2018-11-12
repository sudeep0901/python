class MyClass:

    def method(self):
        return "installnce method called"

    @classmethod
    def classmethod(cls):
        return "class method called"

    @staticmethod
    def staticmethod(val):
        value = val
        return "static method called" + str(value + 1)


myobj = MyClass()

print(myobj.__class__())
print(myobj.staticmethod(5))
print(MyClass.classmethod())

print(MyClass.staticmethod(5))

myobj1 = MyClass()
print(myobj1.staticmethod(5))


# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients

#     def __repr__(self):
#         return f'Pizza({self.ingredients!r})'


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


Pizza(['cheese', 'tomatoes'])

str(Pizza)
Pizza.margherita()


Pizza.prosciutto()

repr(Pizza)
