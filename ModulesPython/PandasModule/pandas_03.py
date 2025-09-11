import pandas as pd

df = pd.read_csv("D:\Python_dataAnalytics\Operations_data\hotel_booking.csv")

# print(df.columns)
# print(df.shape)
# print(df.size)
# print(df.head())
# print(df.head(10))
# print(df.tail()) #last 5 rows
# print(df.describe())  #all statistical value provide
print(df.info())