%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from numpy import nan
#  With any of the preceding examples, it can quickly become tedious to do the transformations by hand, especially if you wish to string together multiple steps. For example, we might want a processing pipeline that looks something like this:

# Impute missing values using the mean
# Transform features to quadratic
# Fit a linear regression

# To streamline this type of processing pipeline, Scikit-Learn provides a Pipeline object, which can be used as follows:
from sklearn.preprocessing import PolynomialFeatures

from sklearn.pipeline import make_pipeline
X = np.array([[ nan, 0,   3  ],
              [ 3,   7,   9  ],
              [ 3,   5,   2  ],
              [ 4,   nan, 6  ],
              [ 8,   8,   1  ]])
y = np.array([14, 16, -1,  8, -5])

model = make_pipeline(Imputer(strategy='mean'),
                      PolynomialFeatures(degree=2),
                      LinearRegression())


model.fit(X, y)  # X with missing values, from above
print(y)
print(model.predict(X))
