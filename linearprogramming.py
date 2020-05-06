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
ecuaciones =[]
color = "b"
rango =3
#matriz que tendrá las variables de decisión y las restricciones
matriz = np.matrix([[5,15,50],[20,5,40],[15,2,60]] ) #matriz de 3xn donde se almacenan las restricciones
for i in range(rango): #range(n) donde n son las restricciones 
    tpx=0
    tpy=0
    xx1=-1
    yy1=-1
    if(matriz[i,0]==0): #en caso tengamos una f(x)=n
        temp = matriz[i,2]/matriz[i,1] #temp dividirá los valores para las gráficas
        parejas.append('10')
        hlines(y=temp,xmin=0,xmax=10,color="b")  #como f(x)=n es una linea vertical u horizontal dibujamos la línea
        xplot=[0,0]#establecemos X y Y como parejas cartesianas
        tpx=temp
        
    else:
        x=matriz[i,2]/matriz[i,0] #aquí si no se cumple nada de lo anterior dividimos normalmente 
        parejas.append(str(x))
        xplot=[x,0]#establecemos X y Y como parejas cartesianas
        tpx=x
        xx1=0 #banera x para plotear el punto
        
    if(matriz[i,1]==0):
        temp = matriz[i,2]/matriz[i,0]
        parejas.append('10')
        vlines(x=temp,ymin=0,ymax=10,color="g")
        yplot=[0,0]
        tpy=temp
        
        
    else:
        y=matriz[i,2]/matriz[i,1]
        parejas.append(str(y))
        yplot=[0,y]
        tpy=y
        yy1=0
    plt.title("Solucion por Método Gráfico")
    if xx1==0:    
        plot(tpx,0,'ro')
        
    if yy1==0:
        plot(0,tpy,'ro')
        
    plot(tpx,tpy,0)
    
    plot(xplot,yplot,color="r", label="ecuacion") #ploteamos la/s linea/s 
    plt.axhline(0,color="black")
    plt.axvline(0,color="black")
#ecuaciones de las rectas
for x in range(0,(rango*2),2):
    print('(',parejas[x],',',parejas[x+1],')')
    frmX=parejas[x]
    frmY=parejas[x+1]
    m=float(frmY)/(float(frmX)*-1)
    b=m*float(float(frmX)*-1)
    ecuaciones.append(str(m))
    ecuaciones.append(str(b))

print(ecuaciones)
#hallar y graficar puntos de interseccion    
for x in range(0,(rango*2),2):
    for y in range(0,(rango*2),2):
        if x==y:
            continue
        mx=((float(ecuaciones[x])*-1)+(float(ecuaciones[y])))
        B=((float(ecuaciones[x+1])+(float(ecuaciones[y+1])*-1)))
        ipx= B/mx
        ipy=((float(ecuaciones[x])*float(ipx))+float(ecuaciones[x+1]))
        print(str(ipx),str(ipy))
        if ipx >0 and ipy >0:
            plot(ipx,ipy,'ro')
    
    
    
    
    
    
show()    
