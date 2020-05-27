#importación de Librerías
from pylab import *
import numpy as np
import matplotlib.pyplot as plt 
#dibujamos los límites del plano cartesiano
plt.axhline(0,color="black")
plt.axvline(0,color="black")
#variables de Z


zA=0.4
zB=0.5

b=0 #bandera del array para la cuenta 
leyenda=""
parejas=[]
ecuaciones =[]
constantes=[]
color = "b"
rango =3
#matriz que tendrá las variables de decisión y las restricciones
matriz = np.matrix([[0.3,0.1,2.7],[0.5,0.5,6],[0.6,0.4,6]] ) #matriz de 3xn donde se almacenan las restricciones
restricciones=('0','1','2',) #donde (0,<)(1,=)(2,>)
for i in range(rango): #range(n) donde n son las restricciones 
    tpx=0
    tpy=0
    xx1=-1
    yy1=-1
    bipx=-1
    bipy=-1
    if(matriz[i,0]==0): #en caso tengamos una f(x)=n
        temp = matriz[i,2]/matriz[i,1] #temp dividirá los valores para las gráficas ymaxima en funcion constante
        parejas.append(matriz[i,2])
        hlines(y=temp,xmin=0,xmax=matriz[i,2],color="b")  #como f(x)=n es una linea vertical u horizontal dibujamos la línea
        xplot=[0,0]#establecemos X y Y como parejas cartesianas
        tpx=temp
        bipx=1 #bandera para puntos de intersección
        constantes.append(str(tpx))
        
        
    else:
        x=matriz[i,2]/matriz[i,0] #aquí si no se cumple nada de lo anterior dividimos normalmente 
        parejas.append(str(x))
        xplot=[x,0]#establecemos X y Y como parejas cartesianas
        tpx=x
        xx1=0 #banera x para plotear el punto
        
    if(matriz[i,1]==0):
        temp = matriz[i,2]/matriz[i,0]
        parejas.append(matriz[i,2])
        vlines(x=temp,ymin=0,ymax=matriz[i,2],color="g")
        yplot=[0,0]
        tpy=temp
        bipy=1
        
        constantes.append(str(tpy))
        
        
    else:
        y=matriz[i,2]/matriz[i,1]
        parejas.append(str(y))
        yplot=[0,y]
        tpy=y
        yy1=0
    plt.title("Solucion por Método Gráfico")
    
    if xx1==0:    
        plot(tpx,0,'ro')
        z=((zA*float(tpx))+0)
        #condiciones para las soluciones
        if restricciones[i]=='0':
            if z<=matriz[i,2]:
                leyenda=("(x1,x2)="+"("+str(round(tpx,2))+","+str(round(0,2))+") con Z="+str(round(z,2)))
        elif restricciones[i]=='1':
            if z==matriz[i,2]:
                leyenda=("(x1,x2)="+"("+str(round(tpx,2))+","+str(round(0,2))+") con Z="+str(round(z,2)))
        elif restricciones[i]=='2':
            if z >= matriz[i,2]:
                leyenda=("(x1,x2)="+"("+str(round(tpx,2))+","+str(round(0,2))+") con Z="+str(round(z,2)))
        
        punto='('+str(round(tpx,2))+','+str(round(0,2))+')'
        plt.annotate(punto,(tpx,0),fontsize="x-small")
        #plot(0,0,color="white",label=leyenda)#mandamos la respuesta a una leyenda en la esquina superior izquierda
        #legend(loc='upper-left',title="Área de Soluciones")
        
    if yy1==0:
        plot(0,tpy,'ro')
        z=(0+(zB*float(tpy)))
        if restricciones[i]=='0':
            if z<=matriz[i,2]:
                    leyenda=("(x1,x2)="+"("+str(round(0,2))+","+str(round(tpy,2))+") con Z="+str(round(z,2)))
        elif restricciones[i]=='1':
            if z==matriz[i,2]:
                    leyenda=("(x1,x2)="+"("+str(round(0,2))+","+str(round(tpy,2))+") con Z="+str(round(z,2)))
        elif restricciones[i]=='2':
            if z >= matriz[i,2]:
                leyenda=("(x1,x2)="+"("+str(round(0,2))+","+str(round(tpy,2))+") con Z="+str(round(z,2)))
        
        punto='('+str(round(0,2))+','+str(round(tpy,2))+')'
        plt.annotate(punto,(0,tpy),fontsize="x-small")
    #   plot(0,0,color="white",label=leyenda)#mandamos la respuesta a una leyenda en la esquina superior izquierda
    #   legend(loc='upper-left',title="Área de Soluciones")
        
        
    plot(tpx,tpy,0)
    
    plot(xplot,yplot,color="r") #ploteamos la/s linea/s 
    plt.axhline(0,color="black")
    plt.axvline(0,color="black")
#ecuaciones de las rectas

for x in range(0,(rango*2),2):
    frmX=float(parejas[x])
    frmY=float(parejas[x+1])
    
    m=float(frmY)/(float(frmX)*-1)
    b=m*float(float(frmX)*-1)
    ecuaciones.append(str(m))
    ecuaciones.append(str(b))


#hallar y graficar puntos de interseccion   

for x in range(0,(rango*2),2):
    for y in range(0,(rango*2),2):
        if x==y:
            continue
        
        mx=((float(ecuaciones[x])*-1)+(float(ecuaciones[y])))
        B=((float(ecuaciones[x+1])+(float(ecuaciones[y+1])*-1)))
        if mx==0:
            ipx=0
        else:
            ipx= (B/mx)
        ipy=((float(ecuaciones[x])*float(ipx))+float(ecuaciones[x+1]))
        
        #calculos de intersección
        if ipx >0 and ipy >0: #and bipx<0 and bipy<0:
            plot(ipx,ipy,'ro')
            punto='('+str(round(ipx,2))+','+str(round(ipy,2))+')'
            plt.annotate(punto,(ipx,ipy),fontsize="x-small")
            z=((zA*float(ipx))+(zB*float(ipy)))
            leyenda=("(x1,x2)="+"("+str(round(ipx,2))+","+str(round(ipy,2))+") con Z="+str(round(z,2)))#respuestas
            plot(0,0,color="white",label=leyenda)
            legend(loc='upper-left',title="Área de Soluciones")
        
  
show()


