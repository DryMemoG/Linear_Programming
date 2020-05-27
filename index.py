from flask import Flask, render_template, request, redirect, url_for
from scipy.optimize import linprog
import numpy as np
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
    A_ub = np.array(d).reshape(len(c),int(len(d)/len(c)))
    
     
    #A_ub=[[1,4,8],[40,30,20],[3,2,4]]
    vsol = request.form['vsolucion']
    vssplit = vsol.split(',')
    b_ub=[int(x) for x in vssplit]
    esim = request.form['esimple']
    esimsplit = esim.split(',')
    A_eq=[[int(x) for x in esimsplit]]
    resu=request.form['resultado']
    ressplit = resu.split(',')
    b_eq=[int(x) for x in ressplit]
    res = linprog(c,A_ub,b_ub,A_eq,b_eq,bounds=(0,None))
    solucion = "Valor óptimo: "+str(res.fun)+"\nX: "+str(res.x)
    return render_template("msimplexsol.html",res=solucion)
    
@app.route("/granm",methods=["GET", "POST"])

def fnMGM():
    return render_template("GMdatos.html")
@app.route("/granmsol", methods=["GET", "POST"])
def fnGMsol():
    cantrest = request.form['objetivo']
    cadenasplit = cantrest.split(',')
    c =[int(x) for x in cadenasplit]
    
    restricc = request.form['restricc']
    rsplit = restricc.split(',')
    d = [int(x) for x in rsplit]
    A_ub = np.array(d).reshape(len(c),int(len(d)/len(c)))
    
     
    #A_ub=[[1,4,8],[40,30,20],[3,2,4]]
    vsol = request.form['vsolucion']
    vssplit = vsol.split(',')
    b_ub=[int(x) for x in vssplit]
    esim = request.form['esimple']
    esimsplit = esim.split(',')
    A_eq=[[int(x) for x in esimsplit]]
    resu=request.form['resultado']
    ressplit = resu.split(',')
    b_eq=[int(x) for x in ressplit]
    res = linprog(c,A_ub,b_ub,A_eq,b_eq,bounds=(0,None))
    solucion = "Valor óptimo: "+str(res.fun)+"\nX: "+str(res.x)
    return render_template("GMsol.html",res=solucion)

if __name__ == "__main__":
    app.run(debug=True)
