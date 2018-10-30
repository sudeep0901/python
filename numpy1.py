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
