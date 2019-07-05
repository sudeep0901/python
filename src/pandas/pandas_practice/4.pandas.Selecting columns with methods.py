import pandas as pd

movie = pd.read_csv(r"D:\github\python\src\pandas\data\movie.csv")
print(movie.head())
 
movie.dtypes

movie.get_dtype_counts()

movie_actor_director = movie[['actor_1_name', 'actor_2_name',
'actor_3_name', 'director_name']]

movie_actor_director.head()

# Step 2 shows how to select a single column as a DataFrame rather than as a Series. Most
# commonly, a single column is selected with a string, resulting in a Series. When a
# DataFrame is the desired output, simply put the column name in a single-element list.
#returns dataframe
type(movie[['director_name']])
#return series
type(movie['director_name'])

movie
movie.select_dtypes(include=['int','float']).head()

# If you would like to select all the numeric columns, you may simply pass the
# string number to the include parameter:

movie.select_dtypes(include=['number']).head()
movie.select_dtypes(include=['object']).head()

# we use the like parameter to search for all column
# names that contain the exact string, facebook:
movie.filter(like='facebook').head()
# we search for all columns that have a digit
# somewhere in their name:
# exclusive parameters, items, like, and regex
movie.filter(regex='\d').head()

movie.filter(like='a',axis=0).head()

# The filter method comes with another parameter, items, which takes a list of exact
# column names. This is nearly an exact duplication of the indexing operator, except that a
# KeyError will not be raised if one of the strings does not match a column name. For
# instance, movie.filter(items=['actor_1_name', 'asdf']) runs without error and
# returns a single column DataFrame.

movie
movie.filter(items=['director_name','num_critic_for_reviews']).head()

# Ordering column names sensibly

set(movie.columns) == set(movie.columns)

['a', 'b'] + ['c' , 'd']

movie.shape
movie.ndim
movie.size
movie.count()
movie.min
movie.min(skipna=False)

movie.isnull().sum()
movie.isnull().sum().sum()
movie.isnull().any().any()

movie.isnull().get_dtype_counts()
movie.isnull()
movie.select_dtypes(['object']) \
.fillna('') \
.min()