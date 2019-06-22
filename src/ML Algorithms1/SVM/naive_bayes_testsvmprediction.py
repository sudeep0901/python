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
from sklearn.externals import joblib


#print (sys.argv[1])
#print (sys.argv[2])
#nltk.download()
global inputfile
inputfile =pd.read_csv(r"D:\svnTicketDispatcher\Inex Ticket Dispatcher\data\test_data Anapalara\excel\Inex_test_data_1.csv", encoding='ISO-8859-1')


eng_stopwords   = set(stopwords.words('english'))
 

#print(feature_train)
CountVectorizer  = CountVectorizer(encoding='ISO-8859-1', stop_words='english')
feature_train = joblib.load(r'D:\svnTicketDispatcher\feature_train.sav')

xtrainCounts = CountVectorizer.fit_transform(feature_train)

print(xtrainCounts)

print(datetime.now())    
print("Starting TFIDF...")

tfidf = TfidfTransformer()
xtrainTfidf = tfidf.fit_transform(xtrainCounts)

# ## SVM
print(datetime.now())    
print("Starting Training...")

clfSVM = joblib.load(r'D:\svnTicketDispatcher\svm_mode.sav')

print(datetime.now())    
print("Starting Prediction...")

global ft
ft = inputfile
ft = ft.replace(np.nan,"", regex=True)
ft1= ft['TICKET_PROBLEM_SUMMARY']
ft2= ft['Assigned Group*+']
ft3= ft['Incident ID*+']
  
xNewCounts = CountVectorizer.transform(ft1)

#print(xNewCounts)
yNewCounts = tfidf.fit_transform(xNewCounts)
#print(yNewCounts)

predictedSVM = clfSVM.predict(yNewCounts)
class_probabilities = clfSVM.predict_proba(yNewCounts) * 100

print(datetime.now())    
print("Finished Prediction...")
outputfileSVM = r"D:\svnTicketDispatcher\Output_SVM.csv"
out_df = pd.DataFrame({"Ticket":ft3, "TICKET_PROBLEM_SUMMARY":ft1, "Assigned Group*+":ft2, "Assignment Group ML":predictedSVM, "Confidence Probability%":(class_probabilities.max(axis=1))})
column_order = ["Ticket","TICKET_PROBLEM_SUMMARY","Assigned Group*+","Assignment Group ML","Confidence Probability%"]
out_df[column_order].to_csv(outputfileSVM, index=False)

