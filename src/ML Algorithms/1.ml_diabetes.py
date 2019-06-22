import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
# https://github.com/JerryKurata/MachineLearningWithPython/


diabetes_data = pd.read_csv(r'src/ML Algorithms/1.ml.pima-data.csv')
# ticket_data = pd.read_csv(r'D:\svnTicketDispatcher\Inex Ticket Dispatcher\data\Inex Remedy Ticket Dump - July to May19\working\1.Inex Ticket Data Merged - July18 to May19.csv')
diabetes_data.head()    
print(diabetes_data.shape)

print(diabetes_data.isnull().values.any())

# checking correlation

def plot_corr(df, size = 11):
    '''funciotn plot correlation betwen feature of dataframe'''
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr) # color code based on the correlation
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()

plot_corr(diabetes_data, len(diabetes_data.columns))
print(diabetes_data.corr())
# plot_corr(ticket_data, len(ticket_data.columns))
# diabetes_data.corr()

del diabetes_data['skin']
diabetes_map = {True:1, False:0}
diabetes_data['diabetes'] = diabetes_data['diabetes'].map(diabetes_map)
print(diabetes_data.head())
num_true = len(diabetes_data.loc[diabetes_data['diabetes'] == True])
num_false = len(diabetes_data.loc[diabetes_data['diabetes']== False])

print(num_true, num_false)
print((num_true / (num_true + num_false)) * 100)
print((num_false / (num_true + num_false)) * 100)
