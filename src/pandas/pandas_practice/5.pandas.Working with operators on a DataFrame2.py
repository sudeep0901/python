import pandas as pd
import numpy as np
college = pd.read_csv("src\pandas\data\college.csv", index_col="INSTNM")
college.columns

college_ugds_ = college.filter(like='UGDS_')

college_ugds_.count(axis=0)
college_ugds_.count(axis=1)
college_ugds_.index
college_ugds_.count(axis='columns').head()

college_ugds_.sum(axis='columns').head()
college_ugds_.median(axis='index')