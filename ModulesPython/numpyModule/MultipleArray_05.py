import numpy as np

a = np.arange(0,18).reshape((6,3))
b = np.arange(20,38).reshape((6,3))

# print(a)
# print(b)

print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a%b)


# for ar dot product / matrix multipication 
c = np.arange(1,17).reshape((4,4))
d = np.arange(21,37).reshape((4,4))

# print(c@d)
# print(c.dot(d))
# print(b.argmax(1))
print(c.max())
print(c.min())
print(c.argmax(1))
print(np.sum(c))
print(np.sum(c, axis=1))
print(np.sum(c, axis= 0))
print(np.mean(c))
print(np.sqrt(c))
print(np.log(c))
