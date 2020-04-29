#import needed for functions
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
x=np.linspace(0,5,10) 
print(x)
print(type(x))
y=x**2
figure()#starts plotting graph
plot(x,y,'r')#plot x& y& 'r'-red
#xlabel('x')
xlabel('timesample')
#ylabel('y')
ylabel('temperature values')
title('my first graph')
show() #mandatory without this wont show output

#subplot-->it is matplotlib function
subplot(1,2,1) #1 row 2 columns 1st one
plot(x,y,'r--') #y wrt x and r-- dashed line in red
subplot(1,2,2) #1 row 2nd column 2nd one
plot(y,x,'g*-') #x wrt y *- style green line
show()