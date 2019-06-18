import matplotlib as mlp
import matplotlib.pyplot as plt
# import random
plt.style.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)

def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
Z = f(X, Y)
plt.contour(X, Y, Z,  cmap="RdGy");
plt.show()
plt.contourf(X, Y, Z,  cmap="RdGy");
plt.colorbar()

plt.show()

plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
cmap='RdGy')
plt.colorbar()
plt.axis(aspect='image');
xvalues = np.array([0, 1, 2, 3, 4]);
yvalues = np.array([0, 1, 2, 3, 4]);
xx, yy = np.meshgrid(xvalues, yvalues)
print(xx, yy)
plt.plot(xx, yy)
plt.show()

contours = plt.contour(X, Y, Z, 3, colors='black')
plt.clabel(contours, inline=True, fontsize=8)
plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
cmap='RdGy', alpha=0.5)
plt.colorbar();
plt.show()