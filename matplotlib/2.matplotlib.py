import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np


plt.style.use("seaborn-whitegrid")
fig = plt.figure()
ax = plt.axes()
# plt.show()

x = np.linspace(0,10, 1000)
ax.plot(x, np.sin(x))
# plt.show()

ax.plot(x, np.cos(x))

# Adjusting the Plot: Line Colors and Styles

ax.plot(x, np.sin(x - 0), color="blue", label='sin(x)')
ax.plot(x, np.sin(x - 1), color="g", label='cos(x)')
ax.plot(x, np.sin(x - 2), color="0.75")
ax.plot(x, np.sin(x - 3), color="#FFDD44")
ax.plot(x, np.sin(x - 4), color=(1.0,0.2, 0.3))
ax.plot(x, np.sin(x - 5), color="chartreuse")
ax.plot(x, np.sin(x - 6), linestyle="dashed")
ax.plot(x, np.sin(x - 7), linestyle=":")
ax.plot(x, np.sin(x - 8), linestyle="-.", label='cos(x)')
ax.plot(x, x + 0.01, '--r') # dashed cyan
ax.set_title("Sinusoidal Graph")
ax.set_xlabel("X")
ax.set_ylabel("sin(x), cos(x)")
ax.set(xlabel="sinx", ylabel="cosx")
line = np.linspace(1, 5, 1000)
ax.plot(line, line + 1 + 0.01,'--g')
plt.xlim(-1,11)
plt.ylim(1.5,11.5)
plt.axis([-1,11,-1.5, 2.5])
# plt.axis('equal')
# plt.xlabel("X")
# plt.ylabel('Sinx & Cosx')
plt.show()

