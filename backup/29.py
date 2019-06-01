import seaborn as sns

iris = sns.load_dataset('iris')
iris.head()

sns.set()
sns.pairplot(iris, hue='species', height=1.5)

#feature matrix
X_iris = iris.drop('species', axis=1)
X_iris.shape

y_iris = iris['species']
y_iris

# target vector
y_iris.shape
y_iris
