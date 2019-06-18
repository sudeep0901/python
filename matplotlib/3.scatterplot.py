import matplotlib as mlp
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
import numpy as np
x = np.linspace(1, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'D',color="red")
plt.show()

rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
    label="marker='{0}'".format(marker))

plt.show()

plt.plot(x, y, '-p', color='gray',
markersize=15, linewidth=4,
markerfacecolor='white',
markeredgecolor='gray',
markeredgewidth=2)
plt.ylim(-1.2, 1.2);
plt.show()