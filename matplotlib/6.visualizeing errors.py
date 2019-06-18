import matplotlib as mlp
import matplotlib.pyplot as plt
# import random
plt.style.use('seaborn-whitegrid')
import numpy as np


# rng = np.random.RandomState(0)
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='.k');
plt.show()
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
ecolor='lightgray', elinewidth=3, capsize=0);
plt.show()