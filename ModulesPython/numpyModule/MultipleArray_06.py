import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
print(pi)

sinN = np.sin((np.pi/2))
print(sinN)

x = np.arange(1,11)
y=np.arange(10,110,10)
plt.figure(figsize= (6,6))
plt.plot(x, y, 'r--')
plt.show()