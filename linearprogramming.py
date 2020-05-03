from pylab import *
import numpy as np
import matplotlib.pyplot as plt 
#dibujamos los límites del plano cartesiano
plt.axhline(0,color="black")
plt.axvline(0,color="black")
#matriz que tendrá las variables de decisión y las restricciones
matriz = np.matrix([[1,0,4],[0,2,12],[3,2,18]] )
for i in range(3):
    x =matriz[i,2]/matriz[i,0]
    y =matriz[i,2]/matriz[i,1]
    xplot=[x,0]
    yplot=[0,y]
    plot(xplot,yplot,color="c")
show()    

"""
x1=6
y1=4
x2=[8,0]
y2=[0,6]


plt.xlim(-0.5,x1+5)
plt.ylim(-0.5,y1+5)
plt.axhline(y=y1,xmin=0,xmax=x1+5,color="blue")
plt.axvline(x=x1,ymin=0,ymax=y1+5,color="red")
plot(x2,y2,color="green")
show()"""
