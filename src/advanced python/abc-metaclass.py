from abc import ABCMeta

class Text(metaclass=ABCMeta):
    pass


print(Text.register(str))
print(isinstance("Is Text", Text))


@Text.register
class  Prose:
    pass

issubclass(Prose, Text)
print(Prose.__mro__)
