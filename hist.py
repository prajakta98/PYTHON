import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
n= np.array([1,1,2,2,2,2,3,4,5,5,6,6,7,8,8,9,9,10,10,10])
print(len(n))
print(min(n))
print(max(n))
print(n)

fig, axes=plt.subplots(figsize=(12,4))
axes.hist(n)
axes.set_title("Histogram1")
axes.set_xlim((min(n), max(n)))
plt.show()