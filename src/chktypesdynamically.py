from numpy.dual import lstsq
line = "sUDEEP,10,20.0005,0"
field_types = [str, int, float, bool]
raw_fields = line.split(',')

print(raw_fields)

fields = [ty(vl) for ty, vl in zip(field_types, raw_fields)]

print(fields)

lst = [11, 1, 2, 3]

print(lst)
del lst[2]
print(lst)

string = " My name is sudeep patel"

lstString = list(string)

lstString.append("Hello")

print(lstString)
print(string)

print(lstString.index("Hello"))

# try:
lstString.remove("Hello")
# except:
#     raise ValueError("error aya")

print(lstString)
print(lstString.sort(key=None, reverse=True)) 
print(lstString)

