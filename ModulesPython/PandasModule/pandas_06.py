import pandas as pd

df = pd.read_csv("D:\DataScienceWithRahul\Operations_data\sample.csv")
# print(df.head())

# print(df.replace(to_replace=26, value=30))
# print(df.replace(to_replace=[26, 27], value=30))
# print(df.replace(to_replace=[26, 27,34,22,21,67,90], value=['A']))
# print(df.replace(to_replace=[26, 27, 34, 22, 21, 67, 90], value=[100, 200, 300, 400, 500, 600]))

# print(df['Physics'].replace(to_replace=[50,51,52,53], value=[100, 200, 300, 400]))

# print(df.replace('[A-Za-z]', 0 ,regex=True))
# print(df.replace({'Physics': '[A-Za-z]', 'Chemistry': '[0-9]'}, 0 ,regex=True))