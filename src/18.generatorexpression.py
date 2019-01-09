# generator expression is an object that carries out the same computation as a list comprehension,
# but which iteratively produces the result.

values = [1, 2, 3, 4]

genexp = (n * n for n in values)
print(genexp)
next(genexp)
next(genexp)
next(genexp)
next(genexp)
next(genexp)
next(genexp)

genlist = list(genexp)
print(genlist)


# Read a file
f = open("data.txt")  # Open a file
lines = (t.strip() for t in f)  # Read lines, strip
# trailing/leading whitespace
comments = (t for t in lines if t[0] == '#')  # All comments
for c in comments:
    print(c)

# a generator funciton can be converted into list using list function
# clist = list(comments)