#importación de Librerías
from pylab import *
import numpy as np
import matplotlib.pyplot as plt 
#dibujamos los límites del plano cartesiano
plt.axhline(0,color="black")
plt.axvline(0,color="black")
#z = Ax+By
#matriz que tendrá las variables de decisión y las restricciones
matriz = np.matrix([[1,0,4],[0,2,12],[3,2,18]] ) #matriz de 3xn donde se almacenan las restricciones
for i in range(3): #range(n) donde n son las restricciones 
    if(matriz[i,0]==0): #en caso tengamos una f(x)=n
        temp = matriz[i,2]/matriz[i,1] #temp dividirá los valores para las gráficas
        hlines(y=temp,xmin=0,xmax=10,color="b")  #como f(x)=n es una linea vertical u horizontal dibujamos la línea
    x =matriz[i,2]/matriz[i,0] #aquí si no se cumple nada de lo anterior dividimos normalmente 
    if(matriz[i,1]==0):
        temp = matriz[i,2]/matriz[i,0]
        vlines(x=temp,ymin=0,ymax=10,color="g")
    y=matriz[i,2]/matriz[i,1]
    xplot=[x,0]#establecemos X y Y como parejas cartesianas
    yplot=[0,y]
    plot(xplot,yplot,color="c") #ploteamos la/s linea/s 
    
    
show()    
