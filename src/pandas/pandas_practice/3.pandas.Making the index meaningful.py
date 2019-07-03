import pandas as pd

movie = pd.read_csv(r"D:\github\python\src\pandas\data\movie.csv")
print(movie.head())

# By default, both set_index and read_csv drop the column used as the index from the
# DataFrame. With set_index, it is possible to keep the column in the DataFrame by setting
# the drop parameter to False.

movie2 = movie.set_index('movie_title')
movie2.index
# convert series to list

index_list = movie2.index.tolist()
column_list = movie2.columns.tolist()
print(column_list)
str_list  = [''.join(item) for item in column_list]
type(str_list)
# Conversely, it is possible to turn the index into a column with the reset_index method.
# This will make movie_title a column again and revert the index back to a RangeIndex.
# reset_index always puts the column as the very first one in the DataFrame, so the
# columns may not be in their original order:

movie2.reset_index()

idx_rename = {'Avatar':'Ratava', 'Spectre': 'Ertceps'}
col_rename = {'director_name':'Director Name',
'num_critic_for_reviews': 'Critical Reviews'}

movie_renamed = movie.rename(index=idx_rename,
columns=col_rename)

movie_renamed.head()

# It is possible to insert a new column into a specific place in a DataFrame besides the end
# with the insert method. The insert method takes the integer position of the new column
# as its first argument, the name of the new column as its second, and the values as its third.
# You will need to use the get_loc Index method to find the integer location of the column
# name.
movie2.columns

new_column_index =  movie2.columns.get_loc('director_name') + 1
new_column_index
movie2.insert(new_column_index,column='my_likes', value=0)
movie2.columns

# delete a column
del movie2['my_likes']