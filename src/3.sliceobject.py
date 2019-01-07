a = [2, 3, 4, 5]
s = repr(a)
print(s, type(s))
print(str(a))
b = eval(s)
print(b, type(b))

x = 5
print(-x , + +x)
print(x)

items = [ 2, 3, 4, 5]

x, y , z, w = items

print(x, y , z, w)

letters = "abc"
x, y, z = letters  # x = 'a', y = 'b', z = 'c'
datetime = ((5, 19, 2008), (10, 30, "am"))
(month, day, year), (hour, minute, am_pm) = datetime
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[::2]  # b = [0, 2, 4, 6, 8 ]
c = a[::-2]  # c = [9, 7, 5, 3, 1 ]
d = a[0:5:2]  # d = [0,2]
e = a[5:0:-2]  # e = [5,3,1]
f = a[:5:1]  # f = [0,1,2,3,4]
g = a[:5:-1]  # g = [9,8,7,6]
h = a[5::1]  # h = [5,6,7,8,9]
i = a[5::-1]  # i = [5,4,3,2,1,0]
j = a[5:0:-1]  # j = [5,4,3,2,1]
