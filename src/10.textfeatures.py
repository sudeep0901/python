# https://jakevdp.github.io/PythonDataScienceHandbook/05.04-feature-engineering.html
# textfeatures

sample = ['problem of evil',
          'evil queen',
          'horizon problem']    

from sklearn.feature_extraction.text import CountVectorizer

vec = CountVectorizer()
X = vec.fit_transform(sample)
vec.get_feature_names()

import pandas as pd

pd.DataFrame(X.toarray(), columns=vec.get_feature_names())

from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
      'This is the first document.',
      'This document is the second document.',
      'And this is the third one.',
      'Is this the first document?',
  ]

corpus


vec = TfidfVectorizer()

X = vec.fit_transform(sample)
vec.get_feature_names()

X =vec.fit_transform(corpus)
vec.get_feature_names()

pd.DataFrame(X.toarray(),columns = vec.get_feature_names())
vec.get_stop_words()

def savePrint():
    print("Hello fro VIM")

