import pandas as pd

movie = pd.read_csv(r"D:\github\python\src\pandas\data\movie.csv")
print(movie.head())
 
movie.dtypes

movie.get_dtype_counts()