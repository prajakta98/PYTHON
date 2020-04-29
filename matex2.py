import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
x=np.linspace(5,50,150) 
y=3*x+7
figure()
subplot(1,2,1)
plot(x,y,'y+')
subplot(1,2,2)
plot(y,x,'b--')
show()