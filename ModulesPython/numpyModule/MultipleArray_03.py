import numpy as np 

a = np.arange(1,20)
print(a)

b = np.arange(1,19,2)
print(b)

c =b.reshape((3,3))
print(c)

d = b.flatten()
print(d)

e = b.ravel()
print(e)