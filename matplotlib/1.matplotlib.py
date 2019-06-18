import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('classic')

x =  np.linspace(0,10, 100)
plt.plot(x, np.sinc(x))
plt.plot(x, np.cos(x))
plt.show()
fig = plt.figure()

fig.savefig("my_figure.png")
print(fig.canvas.get_supported_filetypes())
# plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))

plt.subplot(2,1,2)
plt.plot(x, np.cos(x))
plt.show()

#Object oriented way
fig, ax = plt.subplots(2)

ax[0].plot(x, np.sin(x))
ax[1].plot(x,np.cos(x))

plt.style.use("seaborn-whitegrid")
ax = plt.axes()