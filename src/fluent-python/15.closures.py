# closures


def make_averagr():
    series = []

    def averager(new_value):
        series.append(new_value)  # free variable
        total = sum(series) / len(series)
        return total

    return averager


# print(locals())


av = make_averagr()

print(av(10))
print(av(11))
print(av.__code__.co_varnames)
# ('new_value', 'total')
print(av.__code__.co_freevars)
# ('series',)
# print(type(av.__code__))
print(av.__closure__, type(av.__closure__))
print(av.__closure__[0].cell_contents, type(av.__closure__))


# The nonlocal Declaration

count = 1000
total = 10000


def make_Averager():
    count = 0
    total = 0

    def averager(new_value):
        # count = count + 1 which is local scope and undefined hence add non local
        # global count, total
        nonlocal count, total

        count += 1
        print(total)
        print(count)

        total += new_value
        return total / count

    return averager


# UnboundLocalError: local variable 'count' referenced before assignment
#
av1 = make_Averager()
print(av1(100))
