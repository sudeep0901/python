# Creating dataframe using dictionary
dict = {
    "Name": ["Sandeep", "Rajesh", "Rakesh", "Ajinkya"],
    "lastname": ["Sharma", "pungliya", "Bhargava", "Rahane"],
    "age": [22, 34, 55, 27], 
    "city":["Indore", "Bhagalpur", "Mumbai", "Pune"], 
    "profession": ["Doctor", "Engineer", "Designer","Player"]
}


import pandas as pd


people = pd.DataFrame(dict)
# print(people)

# adding new column
people['salary'] = 0.00

#adding new column
people.assign(Remarks ="waiting for comments")

people.insert(0,'Insert', 'adding new column using insert method')
print(people.iloc[0])
# print(people.loc['0'])

# set the index
people.index = ["A1", "A2", "A3", "A4"]

print(people)
print("By inhrernt Indexing: ",people.iloc[0])
print(people.loc['A1'])

print(people['Name'])
print(people['Name'],['age'])

print(people[['age']])

print(people[['Name', 'age']])
print(people[0:2])

print(people[2:4])

print("By Column Label:\n", people.loc['A1']['Name'])
print("By Row Label:\n", people.loc['A1'])

# Creating dataframe using dictionary
# dict_1= {
#      ["Sandeep", "Rajesh", "Rakesh", "Ajinkya"],
#      ["Sharma", "pungliya", "Bhargava", "Rahane"],
#      [22, 34, 55, 27], 
#      ["Indore", "Bhagalpur", "Mumbai", "Pune"], 
#       ["Doctor", "Engineer", "Designer","Player"]
# }

# df1 = pd.DataFrame(dict_1)

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data = d)


