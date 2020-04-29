import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
x=np.linspace(2,97,100)
y=-4*x-10
figure()
xlabel('x values')
ylabel('y values')
title('Line Graph')
plot(x,y,'m--')
show()
