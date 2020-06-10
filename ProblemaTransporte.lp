\* Problema_del_Transporte_IO *\
Minimize
Función_Objetivo: 2 Ruta_Cerveceria_1_Bar1 + 4 Ruta_Cerveceria_1_Bar2
 + 5 Ruta_Cerveceria_1_Bar3 + 2 Ruta_Cerveceria_1_Bar4
 + Ruta_Cerveceria_1_Bar5 + 3 Ruta_Cerveceria_2_Bar1 + Ruta_Cerveceria_2_Bar2
 + 3 Ruta_Cerveceria_2_Bar3 + 2 Ruta_Cerveceria_2_Bar4
 + 3 Ruta_Cerveceria_2_Bar5
Subject To
Suma_de_Demanda_Bar_Bar1: Ruta_Cerveceria_1_Bar1 + Ruta_Cerveceria_2_Bar1
 >= 500
Suma_de_Demanda_Bar_Bar2: Ruta_Cerveceria_1_Bar2 + Ruta_Cerveceria_2_Bar2
 >= 900
Suma_de_Demanda_Bar_Bar3: Ruta_Cerveceria_1_Bar3 + Ruta_Cerveceria_2_Bar3
 >= 1800
Suma_de_Demanda_Bar_Bar4: Ruta_Cerveceria_1_Bar4 + Ruta_Cerveceria_2_Bar4
 >= 200
Suma_de_Demanda_Bar_Bar5: Ruta_Cerveceria_1_Bar5 + Ruta_Cerveceria_2_Bar5
 >= 700
Suma_de_Productos_que_salen_Cerveceria_1: Ruta_Cerveceria_1_Bar1
 + Ruta_Cerveceria_1_Bar2 + Ruta_Cerveceria_1_Bar3 + Ruta_Cerveceria_1_Bar4
 + Ruta_Cerveceria_1_Bar5 <= 1000
Suma_de_Productos_que_salen_Cerveceria_2: Ruta_Cerveceria_2_Bar1
 + Ruta_Cerveceria_2_Bar2 + Ruta_Cerveceria_2_Bar3 + Ruta_Cerveceria_2_Bar4
 + Ruta_Cerveceria_2_Bar5 <= 4000
Bounds
0 <= Ruta_Cerveceria_1_Bar1
0 <= Ruta_Cerveceria_1_Bar2
0 <= Ruta_Cerveceria_1_Bar3
0 <= Ruta_Cerveceria_1_Bar4
0 <= Ruta_Cerveceria_1_Bar5
0 <= Ruta_Cerveceria_2_Bar1
0 <= Ruta_Cerveceria_2_Bar2
0 <= Ruta_Cerveceria_2_Bar3
0 <= Ruta_Cerveceria_2_Bar4
0 <= Ruta_Cerveceria_2_Bar5
Generals
Ruta_Cerveceria_1_Bar1
Ruta_Cerveceria_1_Bar2
Ruta_Cerveceria_1_Bar3
Ruta_Cerveceria_1_Bar4
Ruta_Cerveceria_1_Bar5
Ruta_Cerveceria_2_Bar1
Ruta_Cerveceria_2_Bar2
Ruta_Cerveceria_2_Bar3
Ruta_Cerveceria_2_Bar4
Ruta_Cerveceria_2_Bar5
End
