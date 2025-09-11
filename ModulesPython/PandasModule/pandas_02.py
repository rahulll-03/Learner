import pandas as pd 

# lst = [1,2,3,4,5]
# lst = [[1,2,3,4,5],[11,12,13,14,15]]
# df = pd.DataFrame(lst)
# print(df)

# a = pd.Series({'a':1, 'q':2, 'r':3, 's':4, 't':5})
# df = pd.DataFrame(a)
# print(df)

# b = ({'Roll Number': [1,2,3,4,5,6],
#      'Math':[64,33,22,34,90,98],
#      'Physics':[12,22,11,65,33,23]})
# df = pd.DataFrame(b)
# print(df)


c = pd.read_csv('D:\Python_dataAnalytics\Operations_data\hotel_booking.csv')
print(c)