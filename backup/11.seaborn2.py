    import seaborn as sns

iris = sns.load_dataset('iris')
iris.head()

sns.set()
sns.pairplot(iris, hue='species', size=1.5)

#feature matrix
X_iris = iris.drop('species', axis=1)
X_iris.shape

y_iris = iris['species']
y_iris

# target vector
y_iris.shape

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# four features in iris dataset

# reduce dimentionality of iris dataset
# it used more often to visualize the data

# PCA - Principle component Analysis
# and return 2 dimentional data to return

from sklearn.decomposition import PCA

model = PCA(n_components=2) # reduce dimentions to 2 from 4

model.fit(X_iris)
X_2D = model.transform(X_iris)
X_2D

iris['PCA1'] = X_2D[:,0]
iris['PCA2'] = X_2D[:,1]
iris

sns.lmplot("PCA1", "PCA2", hue='species', data=iris, fit_reg=False);

# We see that in the two-dimensional representation, the species are fairly well separated, even though the PCA algorithm had no knowledge of the species labels! This indicates to us that a relatively straightforward classification will probably be effective on the dataset, as we saw before.