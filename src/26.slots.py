import sys
# blank dict is even hefty objects
d = {}
sys.getsizeof(d)

# to resolve hight memory object memory footprint
# use slots
class Resistor:
    __slots__ = ['res_ohms', 'res_tolerance', 'res_watts']
    def __init__(self, res_ohms, res_tolerance, res_watts):
        self.res_ohms = res_ohms
        self.res_tolerance = res_tolerance
        self.res_watts     = res_watts

res = Resistor(10, 5, 0.25)
import sys
# print(sys.getsizeof(res) + sys.getsizeof(res.__dict__))
print(sys.getsizeof(res))

# dynamicall cannot add new attribute dynimcally and __dict__ do not exists when used slots


res.cost_dollars = 0.02
print(sys.getsizeof(res) + sys.getsizeof(res.__dict__))

