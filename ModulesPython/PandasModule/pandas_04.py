import pandas as pd

df = pd.read_csv('D:\Python_dataAnalytics\Operations_data\sample.csv')
# print(df.head())
# print(df.isnull())
# print(df.isnull().sum())
# print(df.isnull().sum().sum())

# dropping the row null values

# print(df.shape)
# print(df.dropna())
# print(df.dropna(axis=1))

# if dropna() means they perform operation on row but if axis=1 then it perform operation on column

# print(df.dropna(how='all'))
# print(df.dropna(how='any'))

# if dropna(how='all') means it will drop the row or column if all the values are null but if how='any' then it will drop the row or column if any value is null

# print(df.dropna(inplace=True))
# if inplace=True then it will modify the original dataframe