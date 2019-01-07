
#%%
import numpy as np
a = np.array([1, 2, 3])
print(a, type(a), type(np.ndarray), type(type))

angles = np.array([0, 30, 45, 60, 90])
print(angles)

print(np.sin(angles))
print(np.sin(angles))

# convert in radians

angles_radians = angles * np.pi/180
print(angles_radians)
print(np.sin(angles_radians))
print(np.radians(angles))
print(np.degrees(angles_radians))

print(np.mean(angles))
print(np.median(angles))

# statistics
salaries = np.genfromtxt('data/salary.csv')
print(salaries)
np.mean(salaries)
np.median(salaries)
np.std(salaries)
salaries.shape
np.var(salaries)
a = np.arange(11) ** 2
a[-2]
a[3:5]
a[:7]
a[:11:2]
a[::-1]  # reverse an array

students = np.array([['Alice', 'Balice', 'Calice ', ' Dalice '], [54, 56, 232, 22], [34, 343, 11, 343]])
print(students)


#%%
students[0]


#%%
students[1]


#%%
students[2]


#%%
students[0:2, 2:4]


#%%
students[:,1:2]


#%%
students[:,1:3]


#%%
students[-1,:]


#%%
students[0,...]


#%%
for i in students:
    print("i =:",i)


#%%
for element in students.flatten():
    print(element)


#%%
for elem in students.flatten(order="F"):
    print(elem)


#%%
x = np.arange(12).reshape(3,4)
x


#%%
for i in np.nditer(x):
    print(i)
    
for i in np.nditer(x, order="F"):
    print(i)


#%%
for arr in np.nditer(x, op_flags = ["readwrite"]):
    arr[...] = arr * arr
x


#%%
a = np.array([['Germany', 'Frane', 'Hungary', "Austria"],
            ['Berlin', 'Paris','Budapest', 'Vienna']])

a


#%%
a.shape


#%%
a.ravel() #copy made if needed


#%%
a.T # transposed Matrix


#%%
a.T.ravel()


#%%
a.reshape(2,4)


#%%
np.arange(15).reshape(3,5)


#%%
np.arange(15).reshape(5,3)


#%%
a.reshape(-1, 2) # -1 special vlaue signified we do ont know rows


#%%
#splitting arrays
arr = np.arange(20)
arr


#%%
np.split(arr, [1, 7])


#%%
p1, p2 = np.hsplit(arr, 2)


#%%
print(p1, p2)

#%% [markdown]
# # Image Manipulation

#%%
from scipy import ndimage
from scipy import misc


#%%
f = misc.face()
f


#%%
f.shape
print(type(f))


#%%
import matplotlib.pyplot as plt
plt.imshow(f)


#%%
plt.imshow(f[100:450,500:1000])


#%%
s1, s2 = np.split(f, 2)
plt.imshow(s1)


#%%
plt.imshow(s2)


#%%
b1 , b2 = (np.split(f, 2,axis=1))
plt.imshow(b1)


#%%
plt.imshow(b2)


#%%
plt.imshow(np.concatenate((b1, b2)))


#%%
plt.imshow(np.concatenate((b1, b2), axis=1))


#%%
# shallow copy of arrays edit will refelect in origional array
fruits = np.array(['Apple', 'Mango', 'WaterMelon', 'Guava'])
f_1 = fruits.view()
f_2 = fruits.view()
print(f_1)
print(f_2)


#%%
id(f_1)


#%%
id(f_2)


#%%
f_1 is fruits


#%%
f_2[2]="Strawberry"
fruits
print(f_1)


#%%
f_1 = np.array(["Chikoo", "papaya"])


#%%
fruits


#%%
np.append(f_1, "New Fruit1")
np.append(f_2, "New Fruit2")


#%%
fruits


#%%
f_2.reshape(2,2)


#%%
# Deep copy
basket = fruits.copy()


#%%
#deep copied 
basket
basket.base is fruits

#%% [markdown]
# # Complex Indexing Using Numpy

#%%
import csv


#%%
a = np.arange(12)**2
a


#%%
indx_1 = [2, 6, 8]


#%%
a[indx_1]


#%%
indx_2 = np.array([[2,4], [8,10]])
indx_2


#%%
a[indx_2] # resulting array is shape is index array


#%%
import pandas as pd

gdp_16 = pd.read_csv("data/gdp_pc.csv")["2016"].values
type(gdp_16)


#%%
gdp_16.shape


#%%
plt.plot(gdp_16)
plt.show()


#%%
np.median(gdp_16)


#%%
gdp_16


#%%
gdp_16 = gdp_16[~np.isnan(gdp_16)] #not nan


#%%
gdp_16


#%%
np.median(gdp_16)


#%%
np.sort(gdp_16)


#%%
np.count_nonzero(gdp_16[gdp_16 > 40000])


#%%
print(np.mean(gdp_16))


#%%
# Indexing withh Boolean arrays


#%%
a = np.arange(16).reshape(4,4)
a


#%%
indx_bool = a > 9


#%%
indx_bool


#%%
a[indx_bool]


#%%
a[indx_bool][0:1]


#%%
np.count_nonzero(a >  6)


#%%
np.sum(a < 6)


#%%
np.sum(a < 6, axis=1)


#%%
np.sum(a < 6, axis=0)


#%%
np.any(a > 8)


#%%
np.all(a < 10)


#%%
np.all(a < 100)


#%%
# indexing structure data
name = ["Alice", "Beth", "Cathy", "Dorothy"]
student_Id =  [1,2, 3,4]
score = [85.4, 90.4, 87.66,78.9 ]


#%%
student_data = np.zeros(4, dtype = {'names':('name', 'studentId','score'),
                                   'formats':('U10', 'i4', 'f8')})


#%%
student_data


#%%
student_data['name'] = name
student_data['studentId'] = student_Id
student_data['score'] = score


#%%
student_data


#%%
student_data[1]


#%%
student_data['name']


#%%
student_data[student_data['score'] > 90]


#%%
# Broadcasting Scalers
# Array multiplying with scaler


