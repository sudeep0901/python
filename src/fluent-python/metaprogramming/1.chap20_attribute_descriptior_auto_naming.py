# To avoid retyping the attribute name in the descriptor declarations, we’ll generate a
# unique string for the storage_name of each Quantity instance.


class Quantity:
    _counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls._counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls._counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):  # self is description instance
        print(type(instance))  # managed instance
        print('property setter called')
        if value > 0:
            # instance.__dict__[self.storage_name] = value
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:

    weight = Quantity()
    print(type(weight), type(Quantity))
    price = Quantity()
    print(id(weight), id(price))

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.price * self.weight


truffle = LineItem('White truffle', 100, 10)
print(truffle.weight, truffle.price)
print(vars(truffle))
print(id(truffle.weight))
print(vars(Quantity))
