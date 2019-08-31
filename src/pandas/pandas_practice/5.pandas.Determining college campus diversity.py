import pandas as pd
import numpy as np
diversity = pd.read_csv(r"src\pandas\data\college_diversity.csv", index_col='School')

diversity.columns
diversity.head()

college = pd.read_csv(r"src\pandas\data\college.csv", index_col='INSTNM')
college_ugds_= college.filter(like='UGDS_')
college.index
college_ugds_.index
college_ugds_.isnull().sum(axis=1).sort_values(ascending=False).head()
college_ugds_.isnull().sum(axis=1)

college_ugds_.isnull()
college_ugds_  = college_ugds_.dropna(how='all')
college_ugds_.isnull().sum(axis=1)
college_ugds_.ge(.15)
diversity_metric = college_ugds_.ge(.15).sum(axis='columns')
diversity_metric.value_counts()
diversity_metric.sort_values(ascending=False).head()
college_ugds_.loc[['Regency Beauty Institute-Austin',
'Central Texas Beauty College-Temple']]

us_news_top = ['Rutgers University-Newark',
'Andrews University',
'Stanford University',
'University of Houston',
'University of Nevada-Las Vegas']

diversity_metric.loc[us_news_top]

(college_ugds_ > .01).all(axis=1).any()