import matplotlib as mlp
import matplotlib.pyplot as plt
import random
plt.style.use('seaborn-whitegrid')
import numpy as np
x = np.linspace(1, 100, 30)
y = np.sin(x)
z= random.sample(range(1, 100), 30)
z
plt.scatter(x, y, marker='o')
plt.show()

plt.scatter(x, z, marker='o')
plt.show()