lsta = [10, 20, 30]
lstb = lsta

print(lsta is lstb)

lstb[2] =500

print(lsta, lstb) # both lists changed as lists are mutable


# To avoid this create a shallow Copy

al = [1, 2, [3, 4]]
bl = list(al) # creating shallow copy but copies object references
print(al is bl)


bl.append(6)
print(al)
print(bl)

bl[2][0] = 500
print(al)
print(bl)
