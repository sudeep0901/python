import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

fig.suptitle("No Axes on this figure")
plt.show()
fig, ax_lst = plt.subplots(4, 4)
plt.show()


