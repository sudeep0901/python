# Descriptors are a way of reusing the same access logic in multiple attributes. For ex‐
# ample, field types in ORMs such as the Django ORM and SQL Alchemy are descriptors,
# managing the flow of data from the fields in a database record to Python object attributes
# and vice versa.
# A descriptor is a class that implements a protocol consisting of the __get__ , __set__ ,
# and __delete__ methods. The property class implements the full descriptor protocol.
# As usual with protocols, partial implementations are OK. In fact, most descriptors we
# see in real code implement only __get__ and __set__ , and many implement only one
# of these methods.

# A class implementing a __get__ , a __set__ , or a __delete__ method is a descriptor.

# We’ll create a Quantity descriptor and the LineItem class will use two instances of
# Quantity : one for managing the weight attribute, the other for price .

# Descriptor class
# A class implementing the descriptor protocol. That’s Quantity in Figure 20-1.
# Managed class
# The class where the descriptor instances are declared as class attributes— LineI
# tem


'''When coding a __set__ method, you must keep in mind what the
 self and instance arguments mean: self is the descriptor in‐
 stance, and instance is the managed instance. Descriptors man‐
 aging instance attributes should store values in the managed in‐
 stances.'''


class Quantity:

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value): # self is description instance
        print(type(instance)) #managed instance
        print('property setter called')
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')


class LineItem:

    weight = Quantity('weight')
    print(type(weight), type(Quantity))
    price = Quantity('price')
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



