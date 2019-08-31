from functools import total_ordering


@total_ordering
class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


print(Number(1) < Number(2))
print(Number(10) > Number(21))
print(Number(10) <= Number(2))
print(Number(10) >= Number(20))
print(Number(2) <= Number(2))
print(Number(2) >= Number(2))
print(Number(2) == Number(2))
print(Number(2) == Number(3))
