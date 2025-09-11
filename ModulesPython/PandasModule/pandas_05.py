import pandas as pd

df = pd.read_csv("D:\DataScienceWithRahul\Operations_data\sample.csv")

# print(df.head())

# print(df.fillna({'Physics': 'none', 'Chemistry': 0}))

# print(df.fillna(method='ffill' ))
# print(df.fillna(method='bfill' ))

# print(df.fillna(method='ffill', axis=0))  
# # column wise
# print(df.fillna(method='bfill', axis=1))
# # row wise
# print(df['Physics'].fillna(value=df['Physics'].mean()))  
# mean value of the column