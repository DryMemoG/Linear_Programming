
from pulp import *
problema=LpProblem("Problema_del_Transporte_IO", LpMinimize)
ofertadores=["Cerveceria 1","Cerveceria 2"]
ofertas=[1000,4000]
oferta=dict(zip(ofertadores,ofertas))
    
demandadores=["Bar1","Bar2","Bar3","Bar4","Bar5"]
demandas=[500,900,1800,200,700]
demanda=dict(zip(demandadores,demandas))

costos=[[2,4,5,2,1],[3,1,3,2,3]]#lista de listas con las variables

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


problema.writeLP("ProblemaTransporte.lp")
problema.solve()
print("Status: {}".format(LpStatus[problema.status]))
for v in problema.variables():
    print("{0:}={1:}".format(v.name,v.varValue))

print("Costo Mínimo: Q.{}".format(problema.objective.value()))