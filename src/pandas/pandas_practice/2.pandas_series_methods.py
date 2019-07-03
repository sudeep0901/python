import pandas as pd

movie = pd.read_csv(r"D:\github\python\src\pandas\data\movie.csv")
print(movie.head())

s_attr_methods = set(dir(pd.Series))
d_attr_methods = set(dir(pd.DataFrame))
print(len(s_attr_methods & d_attr_methods))

director = movie['director_name']
actor_1_facebook_likes =  movie['actor_1_facebook_likes']
actor_1_facebook_likes.dtype
movie.dtypes
movie.get_dtype_counts()

# Series is value_counts, which counts all the occurrences of each unique value
movie['director_name'].value_counts()
actor_1_facebook_likes.value_counts()
actor_1_facebook_likes.mean()
actor_1_facebook_likes.median()
actor_1_facebook_likes.std()
actor_1_facebook_likes.max()
movie[actor_1_facebook_likes == actor_1_facebook_likes.max()]
movie[actor_1_facebook_likes == actor_1_facebook_likes.min()].dropna()
movie[actor_1_facebook_likes == actor_1_facebook_likes.min()]
movie.isna()

director.shape
director.size
# Additionally, there is the useful but confusing count method that returns the
# number of non-missing values:
director.count()
len(director)
len(director.isna())
actor_1_facebook_likes.sum()
actor_1_facebook_likes.describe()
director.describe()

# The quantile method exists to calculate an exact quantile of numeric data:

actor_1_facebook_likes.quantile()
actor_1_facebook_likes.iat[0]

actor_1_facebook_likes.index.min()
actor_1_facebook_likes.index.max()
actor_1_facebook_likes.all()

# Since the count method in step 6 returned a value less than the total number of
# Series elements found in step 5, we know that there are missing values in each
# Series. The isnull method may be used to determine whether each individual
# value is missing or not. The result will be a Series of booleans the same length as
# the original Series:
director_null = director.isnull()
director[director_null == False][:]
# It is possible to replace all missing values within a Series with the fillna
# method:

# From steps 10, 11, and 12, isnull, fillna, and dropna all return a Series.

actor_1_fb_likes_filled = actor_1_facebook_likes.fillna(0)
actor_1_fb_likes_filled
actor_1_facebook_likes_droppedna = actor_1_facebook_likes.dropna()
actor_1_facebook_likes.size
actor_1_facebook_likes.name
actor_1_facebook_likes_droppedna.name = 'actor_1_facebook_likes_droppedna'
actor_1_facebook_likes_droppedna.name
movie.columns[0]
sr = pd.Series([10, 1,10, 1, 10])
sr.quantile(.1)

# The value_counts method is one of the most informative Series methods and heavily used
# during exploratory analysis, especially with categorical columns. It defaults to returning the
# counts, but by setting the normalize parameter to True, the relative frequencies are
# returned instead, which provides another view of the distribution:
director.value_counts(normalize=True)

director.hasnans
director.notnull()

st = set([1, 10, 2, 2,0.3]) # ordered set and unique 

st.add(st.pop())
st

director == 'James Cameron'

imdb_score = movie['imdb_score']
imdb_score.gt(7)
director.eq('James Cameron')

class NumClass():
    def __init__(self, value):
        self.value = value

    def __add__(self,vl):
        print("Add methond called")
        return  vl + 2

nmc = NumClass(10)
nmc+ 100
nmc.value

director.value_counts().head()

