import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
# https://github.com/JerryKurata/MachineLearningWithPython/


diabetes_data = pd.read_csv(r'src/ML Algorithms/1.ml.pima-data.csv')
# ticket_data = pd.read_csv(r'D:\svnTicketDispatcher\Inex Ticket Dispatcher\data\Inex Remedy Ticket Dump - July to May19\working\1.Inex Ticket Data Merged - July18 to May19.csv')
diabetes_data.head()    
print(diabetes_data.shape)

print(diabetes_data.isnull().values.any())

# checking correlation

def plot_corr(df, size = 11):
    '''funciotn plot correlation betwen feature of dataframe'''
    corr = df.corr()
    
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr) # color code based on the correlation
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()

plot_corr(diabetes_data, len(diabetes_data.columns))
print(diabetes_data.corr())
# plot_corr(ticket_data, len(ticket_data.columns))
# diabetes_data.corr()

del diabetes_data['skin']
diabetes_map = {True:1, False:0}
diabetes_data['diabetes'] = diabetes_data['diabetes'].map(diabetes_map)
print(diabetes_data.head())
num_true = len(diabetes_data.loc[diabetes_data['diabetes'] == True])
num_false = len(diabetes_data.loc[diabetes_data['diabetes']== False])

print(num_true, num_false)
print((num_true / (num_true + num_false)) * 100)
print((num_false / (num_true + num_false)) * 100)

#splitting data
from sklearn.cross_validation import train_test_split

feature_col_names = ['num_preg','glucose_conc','diastolic_bp','thickness','insulin','bmi','diab_pred','age',]
predicted_class_names = ['diabetes']
X = diabetes_data[feature_col_names]
print(X, type(X))

#values converts the df object in array
X = diabetes_data[feature_col_names].values
X
y = diabetes_data[predicted_class_names].values

print(X, type(X))
print(y, type(y))
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.30, random_state=42)

print("Total % of training set {}".format((len(X_train)/len(diabetes_data.index)) * 100))
print("Total % of testing set {}".format((len(X_test)/len(diabetes_data.index)) * 100))

## post-split data preparation
diabetes_data.head() # thickness is 0
print("row missing values  {}".format((len(diabetes_data.loc[diabetes_data['glucose_conc'] == 0]))))
print("row missing values  {}".format((len(diabetes_data.loc[diabetes_data['diastolic_bp'] == 0]))))
print("row missing values  {}".format((len(diabetes_data.loc[diabetes_data['thickness'] == 0]))))
print("row missing values  {}".format((len(diabetes_data.loc[diabetes_data['insulin'] == 0]))))
print("row missing values  {}".format((len(diabetes_data.loc[diabetes_data['bmi'] == 0]))))
print("row missing values  {}".format((len(diabetes_data.loc[diabetes_data['diab_pred'] == 0]))))
print("row missing values  {}".format((len(diabetes_data.loc[diabetes_data['age'] == 0]))))
# only insulin can be zero rest is not good data where value are zero

#what to do with missing data
# 1. ignore
# 2. replace with another values mean, median sd impute,
# replace value from expert
# 3. Drop observation

# using mean imputing
from sklearn.preprocessing import Imputer

fill_0 = Imputer(missing_values=0, strategy='mean', axis=0)

X_train = fill_0.fit_transform(X_train)
X_test = fill_0.fit_transform(X_test)

# training initial NB algorithm
from sklearn.naive_bayes import GaussianNB
nb_model =  GaussianNB()
len(X_train)
X_train.shape
len(y_train)
y_train.shape
yt = y_train.ravel()
yt.shape

nb_model.fit(X_train, y_train.ravel())
x = np.array([[1, 2, 3], [4, 5, 6]])
from pprint import pprint
pprint(x.shape) 
pprint(x)
pprint(x.ravel())
pprint(x.ravel().shape)
pprint(x.ravel(order='F'))
pprint(x.ravel(order='K'))
pprint(x.ravel(order='A'))
a = np.arange(12).reshape(2,3,2)
a
a.shape
a_s =  np.arange(12).reshape(2,3,2).swapaxes(1,2)
a_s
pprint(x.reshape(1, 2, 3))
new_a = x.reshape(1, 2, 3)
new_a_1 = new_a.reshape(-1)
new_a_1.reshape(-1)

pprint(x.ravel())
from sklearn.metrics import accuracy_score

predicted_train = nb_model.predict(X_train)
accuracy_score(y_train,predicted_train) *100

predicted = nb_model.predict(X_test)
predicted
from sklearn import metrics
accuracy_score(y_test,predicted) *100
print(accuracy_score(y_test,predicted) *100)

# lets do imputing
print("confusion matrix")
print(metrics.confusion_matrix(y_test,predicted))
print(metrics.classification_report(y_test, predicted))

# try random forest model to improve accuracy

from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train,y_train)
rf_predicted_train = rf_model.predict(X_train)
print(metrics.accuracy_score(y_train, rf_predicted_train))
# 98% accuraccy it is overfitting and will not work well on real world data
rf_predict_test = rf_model.predict(X_test)
print(metrics.accuracy_score(y_test, rf_predict_test))
# 70% accuracy, due to overfitting it works poortly on real world data
print(metrics.confusion_matrix(y_test, rf_predict_test))
print(metrics.classification_report(y_test, rf_predict_test))
# recall and precision more poor

# lets try logistics regression
from sklearn .linear_model import LogisticRegression
lr_model = LogisticRegression(C=0.7, random_state=42)
lr_model.fit(X_train, y_train.ravel())
lr_predicted_test = lr_model.predict(X_test)
print(metrics.accuracy_score(y_test, lr_predicted_test))
print(metrics.classification_report(y_test, lr_predicted_test))

# find values of c for recall improvement
C_start = 0.1
C_end = 5
C_inc =0.1

C_values , recall_scores =[], []

C_val = C_start
best_recall_score = 0
while (C_val < C_end):
    C_values.append(C_val)
    lr_model_loop  =LogisticRegression(C=C_val,random_state=42)
    lr_model_loop.fit(X_train, y_train.ravel())
    lr_predicted_loop_test = lr_model_loop.predict(X_test)
    recall_score = metrics.recall_score(y_test,lr_predicted_loop_test)
    recall_scores.append(recall_score)
    if recall_score > best_recall_score:
        best_recall_score = recall_score
        best_lr_predict_test = lr_predicted_loop_test
    print(C_val, best_recall_score)
    C_val = C_val + C_inc

best_score_C_val = C_values[recall_scores.index(best_recall_score)]
print(best_recall_score, best_score_C_val)

import matplotlib.pyplot as plt

plt.plot(C_values,recall_scores)
plt.xlabel("C value")
plt.ylabel("recall score")
plt.show()


# still 61% may be due to imb alance in dataset
# 65% DIABETICS AND 35% non diabetic and is imbalance of classes
# enabeld wieght hyperparameter to handle unbalance

#balanced weight
# find values of c for recall improvement
# logistic regression with balanced weight to handle class unbalances   
C_start = 0.1
C_end = 5
C_inc =0.1

C_values , recall_scores =[], []

C_val = C_start
best_recall_score = 0
while (C_val < C_end):
    C_values.append(C_val)
    lr_model_loop  =LogisticRegression(class_weight ="balanced" ,C=C_val ,random_state=42)
    lr_model_loop.fit(X_train, y_train.ravel())
    lr_predicted_loop_test = lr_model_loop.predict(X_test)
    recall_score = metrics.recall_score(y_test,lr_predicted_loop_test)
    recall_scores.append(recall_score)
    if recall_score > best_recall_score:
        best_recall_score = recall_score
        best_lr_predict_test = lr_predicted_loop_test
    print(C_val, best_recall_score)
    C_val = C_val + C_inc

best_score_C_val = C_values[recall_scores.index(best_recall_score)]
print(best_recall_score, best_score_C_val)

import matplotlib.pyplot as plt

plt.plot(C_values,recall_scores)
plt.xlabel("C value")
plt.ylabel("recall score")
plt.show()

# lets try logistics regression
from sklearn .linear_model import LogisticRegression
lr_model = LogisticRegression(class_weight="balanced", C=best_recall_score, random_state=42)
lr_model.fit(X_train, y_train.ravel())
lr_predicted_test = lr_model.predict(X_test)
print(metrics.accuracy_score(y_test, lr_predicted_test))
print(metrics.classification_report(y_test, lr_predicted_test))

# use Cross validation 

from sklearn .linear_model import LogisticRegressionCV
lr_model_cv = LogisticRegressionCV(n_jobs=1 ,Cs=3, cv=10 , refit=False, class_weight="balanced", random_state=42)
lr_model_cv.fit(X_train, y_train.ravel())
lr_predicted_cv_test = lr_model_cv.predict(X_test)
print(metrics.accuracy_score(y_test, lr_predicted_cv_test))
print(metrics.classification_report(y_test, lr_predicted_cv_test))
# n_jobs =1 use all the cores in pc
# cs = integer value tries to find best regularizatoin parameter
# CV = 10



