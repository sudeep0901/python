import pandas as pd
import numpy as np
college = pd.read_csv(r"D:\github\python\src\pandas\data\college.csv")
college.columns

college.filter(like='UGDS').isnull().any().any()

college_ugds_ =  college.filter(like='UGDS_')
college_ugds_.head()
college_ugds_ + 5

college_ugds_.isnull()
college_ugds_ // 0.01
college_ugds_.round(2)

# Comparing missing values

np.nan == np.nan # starnge evaluates to False
None == None

np.nan != 5


college = pd.read_csv(r"D:\github\python\src\pandas\data\college.csv", index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')

college_ugds_ == 0.0019

college.equals(college_ugds_)
