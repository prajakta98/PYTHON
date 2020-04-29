import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
x1=np.linspace(5,50,150) 
y1=4*x1-3.5
figure()
subplot(2,2,1)
plot(x1,y1,'b:')
subplot(2,2,2)
plot(y1,x1,'y+')
x2=np.linspace(10,150,70)
y2=x2**3+27*x2**2+13*x2+10
subplot(2,2,3)
plot(x2,y2,'k--')
subplot(2,2,4)
plot(y2,x2,'r*-')
show()