0#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'src/ML Algorithms1/XGBOOST Ensemble Algo Decision tree'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd
from sklearn.model_selection import train_test_split


#%%
from xgboost import XGBClassifier


#%%
data = pd.read_csv("titanic.csv")


#%%
data.head()


