import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# plt.style.use('ggplot')
# plt.style.use('ggplot')
data = np.random.randn(10000)
print(data)
# mpl.rcParams['lines.linewidth'] = 2
# mpl.rcParams['lines.color'] = 'r'
mpl.rc('lines', linewidth=4, color='b')
plt.plot(data)
print(mpl.matplotlib_fname())
plt.show()
#C:\python3.6\lib\site-packages\matplotlib\mpl-data\matplotlibrc
sigma = 1
num_bins = 5

fig, ax = plt.subplots()
data_mean = np.mean(data)
n, bins, patches = ax.hist(data, num_bins, density=1)

mu =  data_mean
# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (num_bins - mu))**2))

ax.plot(num_bins, y, '--')
# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
plt.show()