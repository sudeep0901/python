class LineItem:

    def __init__(self, description, weight, price, volume, defaultprice):
        self.description = description
        self.weight = weight
        self.price = price
        self.volume = volume
        self.__defaultprice = defaultprice

    def get_dprice(self):
        return self.__defaultprice

    def set_dprice(self, value):
        self.defaultprice = value

    def subtotal(self):
        return self.weight * self.price

    def __getattr__(self, name):
        print("property accessed:", name)

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')

# property(fget=None, fset=None, fdel=None, doc=None)

    dprice = property(get_dprice, set_dprice)


walnuts = LineItem("walnuts", 10, 10.00, 25, 1)
print(walnuts.weight)
print(walnuts.volume)
# walnuts = LineItem("walnuts", 0, 10.00)
print(walnuts.__dict__)

print(walnuts.dprice)
print(vars(walnuts))


