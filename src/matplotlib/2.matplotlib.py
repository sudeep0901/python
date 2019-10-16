import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

y = np.linspace(0, 10, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quardatic')
plt.plot(x, x**3, label='cubic')
plt.plot(x, y*x, label='cubic')

plt.ylabel('x label')
plt.ylabel('y label')

plt.title('Simple Plot')
plt.legend()

plt.show()
