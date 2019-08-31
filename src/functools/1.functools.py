from functools import partial


def multiplier(x, y):
    """Multiplier doc string."""
    print(x, y)
    return x * y


double = partial(multiplier, 2)
triple = partial(multiplier, 3)
quadruple = partial(multiplier, 4)
print(double(5))
print(triple(5))
print(triple(quadruple(5)))
print(triple.func)
print(triple.keywords, multiplier.__doc__)
