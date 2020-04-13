import weakref


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Peanut'),
           Cheese('Brie'), Cheese('Parmsan'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese


sorted(stock.keys())
print(stock.keys())

del catalog
print(stock.keys())
sorted(stock.keys())
print(stock.keys())
