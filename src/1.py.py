# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# Feature not linearly explainable
x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 1, 3, 7])
plt.scatter(x, y);


from sklearn.linear_model  import LinearRegression
import numpy as np

X= x[:,np.newaxis]

model  = LinearRegression().fit(X, y)

yfit = model.predict(X)

plt.scatter(x, y)
plt.plot(x, yfit)


# It's clear that we need a more sophisticated model to 
# describe the relationship between x and y.
# One approach to this is to transform the data, adding extra columns of features to drive more flexibility in the model. For example, we can add polynomial features to the data this way:

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)

X2 = poly.fit_transform(X)

print(X2)

model = LinearRegression().fit(X2, y)
yfit =model.predict(X2)

plt.scatter(x, y)
plt.plot(x, yfit)
plt.show()