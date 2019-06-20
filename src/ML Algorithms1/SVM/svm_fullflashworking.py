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


#print (sys.argv[1])
#print (sys.argv[2])
#nltk.download()
global inputfile
inputfile =pd.read_csv(r"excel\Inex_test_data_1.csv", encoding='ISO-8859-1')

#print(inputfile)
global outputfileSVM
outputfileSVM = r"Output_SVM.csv"

global eng_stopwords
eng_stopwords   = set(stopwords.words('english'))
 
#print("inside process")
global trng_dataset
trng_dataset = pd.read_csv(r"_-_ML_Training_Data.csv")

categories = trng_dataset['Assignment_Group']
data = trng_dataset['SUMMARY']
#print(data)

feature_train, feature_test, target_train, target_test = train_test_split(data, categories, test_size=0.0, random_state=42)

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

clfSVM = SVC(C=10000.0, probability=True, verbose=True)
clfSVM = clfSVM.fit(xtrainTfidf, target_train)

#print("here are score")
#print(clfSVM.score(feature_test,target_test))
from sklearn.externals import joblib

joblib.dump(clfSVM, 'svm_mode.sav')
joblib.load(r'svm_mode.sav')

joblib.dump(clfSVM, 'svm_mode.sav')
joblib.load(r'svm_mode.sav')

print(datetime.now())    
print("Starting Prediction...")

global ft
ft = inputfile
ft = ft.replace(np.nan,"", regex=True)
ft1= ft['summary']
ft2= ft['Group']
ft3= ft['Incident ID*+']
  
xNewCounts = CountVectorizer.transform(ft1)

#print(xNewCounts)
yNewCounts = tfidf.fit_transform(xNewCounts)
#print(yNewCounts)

predictedSVM = clfSVM.predict(yNewCounts)
class_probabilities = clfSVM.predict_proba(yNewCounts) * 100

print(datetime.now())    
print("Finished Prediction...")

out_df = pd.DataFrame({"Ticket":ft3, "summary":ft1, "Group":ft2, "Group ML":predictedSVM, "Confidence Probability%":(class_probabilities.max(axis=1))})
column_order = ["Ticket","summary","Group","Group ML","Confidence Probability%"]
out_df[column_order].to_csv(outputfileSVM, index=False)

