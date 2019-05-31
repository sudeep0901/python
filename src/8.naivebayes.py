%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from numpy import nan
import seaborn as sns
# In Depth: Naive Bayes Classification
# Bayesian Classification

# In Bayesian classification, we're interested in finding the probability of a label given some observed features,
# P(L | features)=P(features | L)P(L) /  P(features) L = label
# ll we need now is some model by which we can compute P(features | Li) for each label. Such a model is called a generative model because it specifies the hypothetical random process that generates the data.
#  Specifying this generative model for each label is the main piece of the training of such a Bayesian classifier. 
# but we can make it simpler through the use of some simplifying assumptions about the form of this model.

# This is where the "naive" in "naive Bayes" comes in: if we make very naive assumptions about the generative model for each label, we can find a rough approximation of the generative model for each class, and then proceed with the Bayesian classification. Different types of naive Bayes classifiers rest on different naive assumptions about the data,

# Gaussian Naive Bayes
# In this classifier, the assumption is that data from each label is drawn from a simple Gaussian distribution.

from sklearn.datasets import make_blobs
X, y = make_blobs(1000, 2, centers=2, random_state=2, cluster_std=1.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu');


# One extremely fast way to create a simple model is to assume that the data is described by a Gaussian distribution with no covariance between dimensions. This model can be fit by simply finding the mean and standard deviation of the points within each label, which is all you need to define such a distribution.
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X, y)
rng = np.random.RandomState(0)

Xnew = [-6, -14] + [14, 18] * rng.rand(2000, 2)
Xnew
ynew = model.predict(Xnew)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
lim = plt.axis()
plt.scatter(Xnew[:, 0], Xnew[:, 1], c=ynew, s=20, cmap='RdBu', alpha=0.1)
plt.axis(lim);

yprob = model.predict_proba(Xnew)
yprob

# Multinomial Naive Bayes
# The Gaussian assumption just described is by no means the only simple assumption that could be used to specify the generative distribution for each label. Another useful example is multinomial naive Bayes, where the features are assumed to be generated from a simple multinomial distribution. The multinomial distribution describes the probability of observing counts among a number of categories, and thus multinomial naive Bayes is most appropriate for features that represent counts or count rates.
# Example: Classifying Text¶

from sklearn.datasets import fetch_20newsgroups
data = fetch_20newsgroups()
data.target_names
type(data)
print(data.keys())
data['filenames']
data['target_names']
data['target']
import pandas as pd

categories = ['talk.religion.misc', 'soc.religion.christian',
              'sci.space', 'comp.graphics']

train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

print(train.data[1])
print(test.data[2])

from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.naive_bayes    import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train.data, train.target)
labels = model.predict(test.data)
labels

# estimating performance of algo
from sklearn.metrics import confusion_matrix
mat = confusion_matrix(test.target, labels)
mat
labels
test.target
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=train.target_names, yticklabels=train.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label');

def predict_category(s, train=train, model=model):
    pred = model.predict([s])
    print(pred.shape)
    return train.target_names[pred[0]]


predict_category('sending a payload to the ISS')
predict_category('discussing islam vs atheism')
predict_category('sudeep')
predict_category('determining the screen resolution')
'
# hey are extremely fast for both training and prediction
# They provide straightforward probabilistic prediction
# They are often very easily interpretable
# They have very few (if any) tunable parameters'
