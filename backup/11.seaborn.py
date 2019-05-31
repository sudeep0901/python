# Unsupervised learning: Iris clustering¶
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
from sklearn.decomposition import PCA

model = PCA(n_components=2) # reduce dimentions to 2 from 4

model.fit(X_iris)
X_2D = model.transform(X_iris)
X_2D

iris['PCA1'] = X_2D[:,0]
iris['PCA2'] = X_2D[:,1]
iris

sns.lmplot("PCA1", "PCA2", hue='species', data=iris, fit_reg=False);
# Unsupervised learning: Iris clustering¶
# gaussian mixer Model
from sklearn.mixture import GaussianMixture 
model = GaussianMixture(n_components=3,
            covariance_type='full')
model.fit(X_iris)
y_gmm = model.predict(X_iris)
y_gmm
iris['cluster'] = y_gmm
sns.lmplot("PCA1", "PCA2", data=iris, hue='species',
           col='cluster', fit_reg=False);