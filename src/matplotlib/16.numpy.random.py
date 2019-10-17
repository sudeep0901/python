import numpy as np 
import matplotlib.pyplot as plt

print(np.random.rand(10))

# for i in range(10):
#     rand10 = np.random.rand(10)
#     plt.plot(rand10)
#     plt.show()

rand10 = np.random.rand(10)

rand10n = np.random.randn(1000)

plt.plot(rand10n)
plt.show()

rand10new = np.random.randint(100)
print(rand10new)
plt.plot(rand10new)
plt.show()

