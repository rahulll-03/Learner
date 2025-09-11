import pandas as pd

# print(pd.__version__)
# lst = [1,2,3,4,5,6]
Series = pd.Series(['a','b','c','d','e'],index=[1,2,3,4,5], name = "data")
print(Series)
print(type(Series))

scaler_series = pd.Series(0.5, index=[1,2,3])
print(scaler_series)

# dict_series = pd.Series({'a':1, 'q':2, 'r':3, 's':4, 't':5})
dict_series = pd.Series({'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9],'d':[10,11,12],'e':[13,14,15]})
print(dict_series)
print(dict_series['a'])
print(dict_series[0:3])