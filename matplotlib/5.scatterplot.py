import matplotlib as mlp
import matplotlib.pyplot as plt
# import random
plt.style.use('seaborn-whitegrid')
import numpy as np


rng = np.random.RandomState(0)

x = rng.randn(100)
x
y = rng.randn(100)
colors =rng.randn(100)
sizes = 1000 * rng.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
cmap='viridis')
plt.colorbar(); # show color scale
plt.show()


from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T
plt.scatter(features[0], features[1], alpha=0.2,
s=100*features[3], c=iris.target, cmap='viridis')
plt.colorbar(); # show color scale
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);
plt.show()
