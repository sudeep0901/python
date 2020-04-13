# The first argument of the qty_getter could be named self , but that would be
# strange because this is not a class body; instance refers to the LineItem instance
# where the attribute will be stored.

def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        super().__setattr__(name, value)

        print(name, value)

nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)

print(nutmeg.weight, nutmeg.price)
print(sorted(vars(nutmeg).items()))

print(getattr(nutmeg, 'price'))
print(getattr(nutmeg, 'weight'))
vars(nutmeg)
setattr(nutmeg, 'desc', 'dynamic attribute')
print(getattr(nutmeg, 'desc'))
print(getattr(nutmeg, 'desc'))
print(nutmeg.description)
print(nutmeg.desc)