import pandas as pd


df = pd.read_csv("D:\DataScienceWithRahul\Operations_data\sample2.csv" , index_col='Roll No.')


# loc means location and index column provided to the dataframe
# iloc means index location and index column not provided to the dataframe
# print(df.head())

# print(df.loc[1])
#  the row with index 1

# print(df.loc[[1,2,3,4,5]]) 

# print(df.loc[1:5])
# print(df.loc[1:5 ,'Chemistry'])

# print(df.loc[df['Physics']>80])
# print(df.loc[df['Physics']>80],['Maths'])


# iloc means index location and index column not provided to the dataframe

# print(df.iloc[0])

# iloc[0] means first row

# print(df.iloc[[0]])
# iloc[[0]] means first row in the form of dataframe

# print(df.iloc[[0,1,2,3,4]])
#  iloc[[0,1,2,3,4]] means first 5 rows in the form of dataframe

# print(df.iloc[:,0])
# iloc[:,0] means all rows of first column

# print(df.iloc[:,1])
# iloc[:,1] means all rows of second column