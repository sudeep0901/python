import math

class Pizza:
    def __init__(self, ingredients):
        # self.radius = radius
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


    def __repr__(self):
        # return (f'Pizza({self.radius!r}, '
                # f'{self.ingredients!r})')
        pass

    # def area(self):
    #     return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = Pizza(['mozzarella', 'tomatoes'])
# p.area()

p1 = Pizza.margherita()
# print(p1)



p3= Pizza(['c'])
val = p3.margherita()
# print(val)