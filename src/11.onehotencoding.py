data = [
    {'price': 850000, 'rooms': 4, 'neighborhood': 'Queen Anne'},
    {'price': 700000, 'rooms': 3, 'neighborhood': 'Fremont'},
    {'price': 650000, 'rooms': 3, 'neighborhood': 'Wallingford'},
    {'price': 600000, 'rooms': 2, 'neighborhood': 'Fremont'}
]
data
# {'Queen Anne': 1, 'Fremont': 2, 'Wallingford': 3};
# It turns out that this is not generally a useful approach in Scikit-Learn: the package's models make the fundamental assumption that numerical features reflect algebraic quantities. Thus such a mapping would imply, for example, that Queen Anne < Fremont < Wallingford, or even that Wallingford - Queen Anne = Fremont, which (niche demographic jokes aside) does not make much sense

# use one hot encoding

from sklearn.feature_extraction import  DictVectorizer
vec = DictVectorizer(sparse=False, dtype=int)
vec

vec.fit_transform(data)
vec.get_feature_names()

import pandas as pd


vec = DictVectorizer(sparse=True, dtype=int)
vec

vec.fit_transform(data)
vec.get_feature_names()


# sklearn.preprocessing.OneHotEncoder and sklearn.feature_extraction.FeatureHasher are two additional tools that Scikit-Learn includes to support this type of encoding.
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown='ignore')
Xcat = [['Male', 1], ['Female', 3], ['Female', 2]]
enc.fit(Xcat)
enc.categories_
# enc.fit_transform(data)