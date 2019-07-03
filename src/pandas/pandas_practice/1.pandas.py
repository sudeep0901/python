import pandas as pd

movies_df = pd.read_csv(r"D:\github\python\src\pandas\data\movie.csv")
print(movies_df.head())

print(movies_df.director_name)
print(type(movies_df.director_name))
director_name = movies_df.director_name
len(director_name)
director_name.index
for i in director_name.index:
    print(i)

director_name[director_name.index[10:13]]

movies_df.iloc[1:10]
movies_df['director_name'][1:10]
filmValues = director_name.values
type(filmValues)
filmValues[1:10]

movies_df.values
movies_df.index
movies_df.columns

dir(pd.Series)
movies_df
# movies_df.Year.value_counts()

movies_df.describe()
director_name.size
len(director_name)
director_name.shape

# Additionally, there is the useful but confusing count method that 
# returns the number of non-missing values:

movies_df.count()

index = movies_df.index
columns = movies_df.columns
data = movies_df.values
# RangeIndex, Index, ndarray
print(type(index), type(columns), type(data))
print(issubclass(pd.RangeIndex, pd.Index))
print(columns.values)
print(index.values)

# get the data types of each column in df
print(movies_df.dtypes)
# Use the get_dtype_counts method to return the counts of each data type:
print(movies_df.get_dtype_counts())
print(len(columns))

# movies_df['objects']= [{"name": "Hello i am object"}]
movies_df['objects']= 'sudeep' *10
movies_df['objects']
lisofStrings = "Hi" * 10

director = movies_df['director_name']
print(director.name)
# It is possible to turn this Series into a one-column DataFrame with the to_frame method.
# This method will use the Series name as the new column name:

seriestodf = director.to_frame()
seriestodf.index[0]


