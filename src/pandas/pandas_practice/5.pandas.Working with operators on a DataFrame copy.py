import pandas as pd
import numpy as np
college = pd.read_csv("src\pandas\data\college.csv")
college.columns

college.filter(like='UGDS').isnull().any().any()

college_ugds_ = college.filter(like='UGDS_')
college_ugds_.head()
college_ugds_ + 5

college_ugds_.isnull()
college_ugds_ // 0.01
college_ugds_.round(2)

# Comparing missing values

np.nan == np.nan # starnge evaluates to False
None == None

np.nan != 5


college = pd.read_csv(r"src\pandas\data\college.csv", index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')

college_ugds_ == 0.0019

college.equals(college_ugds_)

college_ugds_.count()
college_ugds_.count(axis=1)
len(college_ugds_.columns)
college_ugds_.sum(axis=0)
college_ugds_

sample = pd.DataFrame([1, 2, 3], [4, 5, 6])
sample

sample.sum(axis=0)
college_ugds_.count(axis='index')
college_ugds_.count(axis='columns').head()
college_ugds_cumsum = college_ugds_.cumsum(axis=1)
college_ugds_cumsum


sample.cumsum(axis=0)

from pandas.testing import assert_frame_equal
assert_frame_equal(college_ugds_, college_ugds_)