import numpy as np
import matplotlib.pyplot as plt


plt.plot([3,5,1,0,5], [31,15,11,0,35], 'ro')
plt.axis([0, 5, 0, 40])
plt.show()


import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 1000

plt.scatter('a', 'b', c='c', s='d', data= data)
plt.xlabel("entty a")
plt.ylabel("entty b")

plt.show()


