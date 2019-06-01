%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from numpy import nan
from sklearn.preprocessing import PolynomialFeatures

X = np.array([[ nan, 0,   3  ],
              [ 3,   7,   9  ],
              [ 3,   5,   2  ],
              [ 4,   nan, 6  ],
              [ 8,   8,   1  ]])
y = np.array([14, 16, -1,  8, -5])

from sklearn.preprocessing import Imputer
imp = Imputer(strategy='mean')

X2 =    imp.fit_transform(X)
X2

model = LinearRegression().fit(X2, y)
model.predict(X2)
