#importación de Librerías
from pylab import *
import numpy as np
import matplotlib.pyplot as plt 
#dibujamos los límites del plano cartesiano
plt.axhline(0,color="black")
plt.axvline(0,color="black")
#z = Ax+By
b=0 #bandera del array para la cuenta 
parejas=[]
color = "b"
#matriz que tendrá las variables de decisión y las restricciones
matriz = np.matrix([[5,15,50],[20,5,40],[15,2,60]] ) #matriz de 3xn donde se almacenan las restricciones
for i in range(3): #range(n) donde n son las restricciones 
    if(matriz[i,0]==0): #en caso tengamos una f(x)=n
        temp = matriz[i,2]/matriz[i,1] #temp dividirá los valores para las gráficas
        parejas.append('largo')
        hlines(y=temp,xmin=0,xmax=10,color="b")  #como f(x)=n es una linea vertical u horizontal dibujamos la línea
        xplot=[0,0]#establecemos X y Y como parejas cartesianas
        
    else:
        x=matriz[i,2]/matriz[i,0] #aquí si no se cumple nada de lo anterior dividimos normalmente 
        parejas.append(str(x))
        xplot=[x,0]#establecemos X y Y como parejas cartesianas
        
    
    if(matriz[i,1]==0):
        temp = matriz[i,2]/matriz[i,0]
        parejas.append('largo')
        vlines(x=temp,ymin=0,ymax=10,color="g")
        yplot=[0,0]
        
    else:
        y=matriz[i,2]/matriz[i,1]
        parejas.append(str(y))
        yplot=[0,y]
        
    
    
    plot(xplot,yplot,color="r") #ploteamos la/s linea/s 
    plt.axhline(0,color="black")
    plt.axvline(0,color="black")
for i in parejas:
    print(i,',')
    
    
    
    
    
show()    
