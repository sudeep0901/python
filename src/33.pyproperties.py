class Celcius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenhiet(self):
        return (self.temperature * 1.8) + 32


man = Celcius()

man.temperature = 37
print(man.temperature, man.to_fahrenhiet())
print((man.__dict__))


class Celcius1:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenhiet(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("getting value")
        return self._temperature
    
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)

    # make empty property
    temperature = property()
    # assign fget
    temperature = temperature.getter(get_temperature)
    # assign fset
    temperature = temperature.setter(set_temperature)
    print(dir(temperature))


c = Celcius1(20)
print(c.__dict__)
print(c.get_temperature())
print(c.temperature)



class Celcius2:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenhiet(self):
        return (self.temperature * 1.8) + 32
    
    @property
    def temperature(self):
        print("getting value")
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("setting values")
        self._temperature = value


