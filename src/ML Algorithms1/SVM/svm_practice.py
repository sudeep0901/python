#Import scikit-learn dataset library
from sklearn import datasets

#Load dataset
cancer = datasets.load_breast_cancer()

print(type(cancer.feature_names), "features:", cancer.feature_names)
print("Labels:", cancer.target_names)
print(cancer.data.shape)
print(cancer.data[0:5,2:10])
print(cancer.target)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.externals import joblib
from sklearn.svm import SVC
from nltk.corpus import stopwords
import pandas as  pd
import numpy as np
from sklearn.model_selection import train_test_split
dataset = pd.read_csv(r"D:\github\python\src\ML Algorithms1\SVM\testdata.csv", encoding='ISO-8859-1')
dataset

categories = dataset['group']
data = pd.Series(dataset[['summary']].fillna('').values.tolist()).str.join(' ')
data
type(dataset[['summary']])
df = pd.DataFrame(["Sudeep                         patel ", "Hello HOw ar eyou"])
df
sr = pd.Series(df[[0]].fillna('').values.tolist()).str.join(' ')
sr

feature_train, feature_test, target_train, target_test = train_test_split(data, categories, test_size=0.0,random_state= 42)
joblib.dump(feature_train, "feature_trained.sav")
type(feature_train)
feature_train
CV = CountVectorizer()
type(feature_train.values.astype('U'))
feature_train
xtraincounts =CV.fit_transform(feature_train.values.astype('U'),target_train)
type(xtraincounts.getcol(0))
print(xtraincounts.getcol(0))
print(CV.get_feature_names())
tfidf = TfidfTransformer()

xtrainTfidf = tfidf.fit_transform(xtraincounts)
xtrainTfidf.toarray()
svm = SVC(C=10000.0, probability=True)
svm.fit(xtrainTfidf, target_train.astype(str))

from sklearn.metrics import accuracy_score
y_test = "sudeep controlm"

df=pd.DataFrame(columns=['TICKET_PROBLEM_SUMMARY'])
df=df.append({'TICKET_PROBLEM_SUMMARY':y_test},ignore_index=True)
print(df['TICKET_PROBLEM_SUMMARY'])
xnewcount = CV.transform(df['TICKET_PROBLEM_SUMMARY'])
print(xnewcount,type(xnewcount), xnewcount[0])
ycount = tfidf.fit_transform(xnewcount)

predicted = svm.predict(ycount)
predicted
cls_probablity = svm.predict_proba(ycount)* 100 
cls_probablity.max(axis=1)
accuracy_score(predicted, df['TICKET_PROBLEM_SUMMARY'])
