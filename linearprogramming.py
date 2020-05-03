from pylab import *

import matplotlib.pyplot as plt 
#x1 será la primera restriccion 
#x2 la segunda que depende de x1 = n y x2=0 

x1=6
y1=4
x2=[8,0]
y2=[0,6]

plt.axhline(0,color="black")
plt.axvline(0,color="black")
plt.xlim(-0.5,x1+5)
plt.ylim(-0.5,y1+5)
plt.axhline(y=y1,xmin=0,xmax=x1+5,color="blue")
plt.axvline(x=x1,ymin=0,ymax=y1+5,color="red")
plot(x2,y2,color="green")
show()
