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

from sklearn.model_selection import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris)
