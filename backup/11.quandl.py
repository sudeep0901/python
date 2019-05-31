import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
df =  quandl.get('WIKI/GOOGL')

df.shape
type(df)
print(df.head())

df = df [['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume' ]]
df.index

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0


# Features
df = df[['Adj. Close', 'HL_PCT', 'PCT_Change', 'Adj. Volume']]

df.head()

# label
forecast_col = 'Adj. Close'
df.fillna(-9999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
df
forecast_out 

df['label'] =  df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
df

x =  np.array(df.drop(['label'], 1))
y =  np.array(df['label'])

x = preprocessing.scale(x)
X = x
# X = x[:-forecast_out + 1]

df.dropna(inplace=True)
y =  np.array(df['label'])
print(len(X), len(y))

X_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = LinearRegression(n_jobs=-1)

clf.fit(X_train, y_train)
clf.score(x_test, y_test)

confidance = clf.score(x_test, y_test)
confidance


clf = svm.SVR()
clf.fit(X_train, y_train)
clf.score(x_test, y_test)

confidance = clf.score(x_test, y_test)
confidance

clf = svm.SVR(kernel="poly")
clf.fit(X_train, y_train)
clf.score(x_test, y_test)

confidance = clf.score(x_test, y_test)
confidance

 