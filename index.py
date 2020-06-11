from flask import Flask, render_template, request, redirect, url_for
from scipy.optimize import linprog
import numpy as np
from pulp import *
app = Flask(__name__)

@app.route("/")

def inicio():
    return render_template("index.html")

@app.route("/mgrafico", methods=["POST", "GET"])

def fnMGrafico():
    
    return render_template("mgrafico1.html")

@app.route("/mgraficosol", methods=["GET", "POST"])

def fnMGraficosol():
    cantrest = request.form['restricts']
    desicion = request.form['desicion']
    return render_template("mgrafico2.html",cant = cantrest,des = desicion)


@app.route("/msimplex", methods=["GET", "POST"])
def fnMSimplex():
    return render_template("simplexdatos.html")

@app.route("/msimplexsol", methods=["GET", "POST"])
def fnMSimplexsol():
    cantrest = request.form['objetivo']
    cadenasplit = cantrest.split(',')
    c =[int(x) for x in cadenasplit]
    
    restricc = request.form['restricc']
    rsplit = restricc.split(',')
    d = [int(x) for x in rsplit]
    A_ub = np.array(d).reshape(int(len(d)/len(c)),len(c))
    
     
    #A_ub=[[1,4,8],[40,30,20],[3,2,4]]
    vsol = request.form['vsolucion']
    vssplit = vsol.split(',')
    b_ub=[int(x) for x in vssplit]
    A_ubt=[]
    b_ubt=[]
    maxmin= request.form['valor']
    if maxmin=="min":
        for x in A_ub:
            x =x*-1
            A_ubt.append(x)
        for y in b_ub:
            y=y*-1
            b_ubt.append(y)
        A_ub=A_ubt
        b_ub=b_ubt
    else:
        A_ub= A_ub
        b_ub=b_ub
    res = linprog(c,A_ub,b_ub,bounds=(0,None))
    solucion = "Valor óptimo: "+str(res.fun)+"\nX: "+str(res.x)
    return render_template("msimplexsol.html",res=solucion)
    
@app.route("/granm",methods=["GET", "POST"])

def fnMGM():
    return render_template("GMdatos.html")
@app.route("/granmsol", methods=["GET", "POST"])
def fnGMsol():
    cantrest = request.form['objetivo']
    cadenasplit = cantrest.split(',')
    c =[int(x) for x in cadenasplit]#corregir como está en pruebapulp
    
    restricc = request.form['restricc']
    rsplit = restricc.split(',')
    d = [int(x) for x in rsplit]
    A_ub = np.array(d).reshape(int(len(d)/len(c)),len(c))
    vsol = request.form['vsolucion']
    vssplit = vsol.split(',')
    b_ub=[int(x) for x in vssplit]
    A_ubt=[]
    b_ubt=[]
    maxmin= request.form['valor']
    if maxmin=="min":
        for x in A_ub:
            x =x*-1
            A_ubt.append(x)
        for y in b_ub:
            y=y*-1
            b_ubt.append(y)
        A_ub=A_ubt
        b_ub=b_ubt
    else:
        A_ub= A_ub
        b_ub=b_ub

     
    #A_ub=[[1,4,8],[40,30,20],[3,2,4]]
    
    
    res = linprog(c,A_ub,b_ub,bounds=(0,None))
    solucion = "Valor óptimo: "+str(res.fun)+"\nX: "+str(res.x)
    return render_template("GMsol.html",res=solucion)

@app.route("/transport")
def fnTDatos():
    return render_template("TPDatos.html")


@app.route("/transportsol",methods=["GET", "POST"])

def transporte():
    problema=LpProblem("Problema_del_Transporte_IO", LpMinimize)
    ofs=request.form['ofertadores']
    ofsplit=ofs.split(',')
    ofertadores=[x for x in ofsplit]

    ofrs=request.form['oferta']
    ofrsplit=ofrs.split(',')
    ofertas=[int(x) for x in ofrsplit]
    oferta=dict(zip(ofertadores,ofertas))
    
    demans=request.form['demandadores']
    dmnsplit = demans.split(',')
    demandadores=[x for x in dmnsplit]
    dems=request.form['demanda']
    
    #c=demandas
    dsplit=dems.split(',')#aqui vamos a dividir la cadena de 1,2,3,4 en un arreglo numerico
    demandas=[int(x) for x in dsplit]#lo guardamos de nuevo en demandas
    demanda=dict(zip(demandadores,demandas))
    #d=costos
    costo=request.form['costos']#llamamos a costos desde el html
    csplit = costo.split(',')#spliteamos
    xx = [int(x) for x in csplit]#ahora es un vector
    costos = np.array(xx).reshape(int(len(xx)/len(demandas)),len(demandas))#aquí ya es una matriz
    #lista de listas con las variables

    costos = makeDict([ofertadores,demandadores],costos,0)
    rutas=[(o,d)for o in oferta for d in demanda]
    cv= LpVariable.dicts("Ruta",(ofertadores,demandadores),0,None, LpInteger)
    problema+=lpSum(costos[o][d]*cv[o][d] for (o,d) in rutas),"Función_Objetivo"

    for o in ofertadores:
        problema+= sum([cv[o][d] for d in demanda]) <= oferta[o], \
                "Suma_de_Productos_que_salen_%s" % o

    for d in demandadores:
        problema += sum([cv[o][d] for o in ofertadores]) >= demanda[d], \
                "Suma_de_Demanda_Bar_%s" % d

    datos = " "
    problema.writeLP("ProblemaTransporte.lp")
    problema.solve()
    print("Status: {}".format(LpStatus[problema.status]))
    for v in problema.variables():
        datos=datos+("{0:}={1:}".format(v.name,v.varValue))+"\n"
        

    
    sol=("Costo Mínimo: Q.{}".format(problema.objective.value()))


    return render_template("TPSol.html", dat=datos,sol=sol)


@app.route("/transportvogel")
def fnTvogelDatos():
    return render_template("TPDatosvogel.html")


@app.route("/transportvogelsol",methods=["GET", "POST"])

def transportevogel():
    problema=LpProblem("Problema_del_Transporte_IO", LpMinimize)
    ofs=request.form['ofertadores']
    ofsplit=ofs.split(',')
    ofertadores=[x for x in ofsplit]

    ofrs=request.form['oferta']
    ofrsplit=ofrs.split(',')
    ofertas=[int(x) for x in ofrsplit]
    oferta=dict(zip(ofertadores,ofertas))
    
    demans=request.form['demandadores']
    dmnsplit = demans.split(',')
    demandadores=[x for x in dmnsplit]
    dems=request.form['demanda']
    
    #c=demandas
    dsplit=dems.split(',')#aqui vamos a dividir la cadena de 1,2,3,4 en un arreglo numerico
    demandas=[int(x) for x in dsplit]#lo guardamos de nuevo en demandas
    demanda=dict(zip(demandadores,demandas))
    #d=costos
    costo=request.form['costos']#llamamos a costos desde el html
    csplit = costo.split(',')#spliteamos
    xx = [int(x) for x in csplit]#ahora es un vector
    costos = np.array(xx).reshape(int(len(xx)/len(demandas)),len(demandas))#aquí ya es una matriz
    #lista de listas con las variables

    costos = makeDict([ofertadores,demandadores],costos,0)
    rutas=[(o,d)for o in oferta for d in demanda]
    cv= LpVariable.dicts("Ruta",(ofertadores,demandadores),0,None, LpInteger)
    problema+=lpSum(costos[o][d]*cv[o][d] for (o,d) in rutas),"Función_Objetivo"

    for o in ofertadores:
        problema+= sum([cv[o][d] for d in demanda]) <= oferta[o], \
                "Suma_de_Productos_que_salen_%s" % o

    for d in demandadores:
        problema += sum([cv[o][d] for o in ofertadores]) >= demanda[d], \
                "Suma_de_Demanda_Bar_%s" % d

    datos = " "
    problema.writeLP("ProblemaTransporte.lp")
    problema.solve()
    print("Status: {}".format(LpStatus[problema.status]))
    for v in problema.variables():
        datos=datos+("{0:}={1:}".format(v.name,v.varValue))+"\n"
        

    
    sol=("Aproximación: Q.{}".format(problema.objective.value()))


    return render_template("TPvogelSol.html", dat=datos,sol=sol)


@app.route("/transportrussell")
def fnTrussellDatos():
    return render_template("TPDatosrussell.html")


@app.route("/transportrussellsol",methods=["GET", "POST"])

def transportrussell():
    problema=LpProblem("Problema_del_Transporte_IO", LpMinimize)
    ofs=request.form['ofertadores']
    ofsplit=ofs.split(',')
    ofertadores=[x for x in ofsplit]

    ofrs=request.form['oferta']
    ofrsplit=ofrs.split(',')
    ofertas=[int(x) for x in ofrsplit]
    oferta=dict(zip(ofertadores,ofertas))
    
    demans=request.form['demandadores']
    dmnsplit = demans.split(',')
    demandadores=[x for x in dmnsplit]
    dems=request.form['demanda']
    
    #c=demandas
    dsplit=dems.split(',')#aqui vamos a dividir la cadena de 1,2,3,4 en un arreglo numerico
    demandas=[int(x) for x in dsplit]#lo guardamos de nuevo en demandas
    demanda=dict(zip(demandadores,demandas))
    #d=costos
    costo=request.form['costos']#llamamos a costos desde el html
    csplit = costo.split(',')#spliteamos
    xx = [int(x) for x in csplit]#ahora es un vector
    costos = np.array(xx).reshape(int(len(xx)/len(demandas)),len(demandas))#aquí ya es una matriz
    #lista de listas con las variables

    costos = makeDict([ofertadores,demandadores],costos,0)
    rutas=[(o,d)for o in oferta for d in demanda]
    cv= LpVariable.dicts("Ruta",(ofertadores,demandadores),0,None, LpInteger)
    problema+=lpSum(costos[o][d]*cv[o][d] for (o,d) in rutas),"Función_Objetivo"

    for o in ofertadores:
        problema+= sum([cv[o][d] for d in demanda]) <= oferta[o], \
                "Suma_de_Productos_que_salen_%s" % o

    for d in demandadores:
        problema += sum([cv[o][d] for o in ofertadores]) >= demanda[d], \
                "Suma_de_Demanda_Bar_%s" % d

    datos = " "
    problema.writeLP("ProblemaTransporte.lp")
    problema.solve()
    print("Status: {}".format(LpStatus[problema.status]))
    for v in problema.variables():
        datos=datos+("{0:}={1:}".format(v.name,v.varValue))+"\n"
        

    
    sol=("Costo: Q.{}".format(problema.objective.value()))


    return render_template("TPrussellSol.html", dat=datos,sol=sol)


if __name__ == "__main__":
    app.run()
