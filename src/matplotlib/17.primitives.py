import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.text as text

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, color='blue', lw=2)

np.random.seed(19680801)
ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
n, bins, pathes = ax2.hist(np.random.randn(
    1000), 50, facecolor='yellow', edgecolor='yellow')
ax2.set_xlabel('time (s)')

print(n, bins, pathes)

for ax in fig.axes:
    ax.grid(True)


l1 = lines.Line2D([0, 1], [0, 1], transform=fig.transFigure, figure=fig)
l2 = lines.Line2D([0, 1], [1, 0], transform=fig.transFigure, figure=fig)

fig.lines.extend([l1, l2])
t1 = text.Text(x=10, y=10, text="Hello Text", color='g')

# fig.texts.extend([t1])
plt.show()
