# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
#import nltk
from nltk.corpus import stopwords 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from datetime import datetime
from sklearn import metrics

from sklearn.externals import joblib

#print (sys.argv[1])
#print (sys.argv[2])
#nltk.download()
global inputfile
inputfile =pd.read_csv(r"excel\test_data_1.csv", encoding='ISO-8859-1')

#print(inputfile)
global outputfileSVM
outputfileSVM = r"D:\root\Output_NB.csv"

global eng_stopwords
eng_stopwords   = set(stopwords.words('english'))
 
#print("inside process")
global trng_dataset
trng_dataset = pd.read_csv(r"D:\root\Inex Ticket Dispatcher\modules\ML\svm\POC\models\INEX_Dispatcher_-_ML_Training_Data.csv")

categories = trng_dataset['GROUP']
data = trng_dataset['SUMMARY']
#print(data)

feature_train, feature_test, target_train, target_test = train_test_split(data, categories, test_size=0.0, random_state=42)
joblib.dump(feature_train, r"\feature_train_naive.sav")

print(datetime.now())    
print("Starting CountVectorizer...")

#print(feature_train)
CountVectorizer  = CountVectorizer(encoding='ISO-8859-1', stop_words='english')
xtrainCounts = CountVectorizer.fit_transform(feature_train)

#print(xtrainCounts)

print(datetime.now())    
print("Starting TFIDF...")

tfidf = TfidfTransformer()
xtrainTfidf = tfidf.fit_transform(xtrainCounts)

## SVM
print(datetime.now())    
print("Starting Training...")

# clfNiaveBayes = SVC(C=10000.0, probability=True, verbose=True)
from sklearn.naive_bayes import BernoulliNB
clfNiaveBayes = BernoulliNB()

clfNiaveBayes = clfNiaveBayes.fit(xtrainTfidf, target_train)

joblib.dump(clfNiaveBayes, r'D:\root\naivebayes_mode.sav')

print("here are score")
print(metrics.accuracy_score(feature_test,target_test))


print(datetime.now())    
print("Starting Prediction...")

global ft
ft = inputfile
ft = ft.replace(np.nan,"", regex=True)
ft1= ft['SUMMARY']
ft2= ft['group*+']
ft3= ft['" " ID*+']
  
xNewCounts = CountVectorizer.transform(ft1)

#print(xNewCounts)
yNewCounts = tfidf.fit_transform(xNewCounts)
#print(yNewCounts)

clfNiaveBayes = joblib.load(r"D:\root\naivebayes_mode.sav")

predictedSVM = clfNiaveBayes.predict(yNewCounts)
class_probabilities = clfNiaveBayes.predict_proba(yNewCounts) * 100

print(datetime.now())    
print("Finished Prediction...")

out_df = pd.DataFrame({"Ticket":ft3, "SUMMARY":ft1, "group*+":ft2, "" "ML":predictedSVM, "Confidence Probability%":(class_probabilities.max(axis=1))})
column_order = ["Ticket","SUMMARY","group*+","ML","Confidence Probability%"]
out_df[column_order].to_csv(outputfileSVM, index=False)

