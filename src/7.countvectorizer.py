from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
vectorizor = CountVectorizer()

sample_text = ["One of the most basic ways we can numerically represent words "
               "is through the one-hot encoding method (also sometimes called "
               "count vectorizing)."]

vectorizor.fit(sample_text)
sample_text = ["sudeep how are you, i am fine?", "patel", "sudeep sudeep sudeep"]
print(sample_text)
vectorizor.fit(sample_text)

print("Vectorizer Vocubalury......................:")
print(vectorizor.vocabulary_)
vector = vectorizor.transform(sample_text)
# print(vector)
print(vector[0][0])
print(vector.toarray())

# Or if we wanted to get the vector for one word:
print('Hot vector: ')
print(vectorizor.transform(['Hot', 'one']).toarray())

# We could also do the whole thing at once with the fit_transform method:
print('One swoop:')
new_text = ['Today is the day day that I do the thing today, today today']
new_vectorizer = CountVectorizer()
print(new_vectorizer.fit_transform(new_text).toarray())

# using on real data

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer


import numpy as np 

vectorizor =  CountVectorizer()

newgroup_data = fetch_20newsgroups()

print(newgroup_data.data[0])

vectorizor.fit(newgroup_data.data)

print("Vocubalary : ..................")
# print(vectorizor.vocabulary_)
print()

v0 = vectorizor.transform([newgroup_data.data[0]]).toarray()[0]
print(v0)

print(len(v0))
print(np.sum(v0))

print(vectorizor.inverse_transform(v0))