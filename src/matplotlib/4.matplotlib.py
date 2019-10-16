import matplotlib.pyplot as plt
import numpy as np


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:


data1, data2, data3, data4 = np.random.randn(4, 100)

print(data1, data2)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data3, {'marker': 'x'})

plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)

my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data4, data2, {'marker': 'o'})
fig.show()
plt.show()
