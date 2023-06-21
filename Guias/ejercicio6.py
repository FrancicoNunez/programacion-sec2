# Existen dos grupos de estudiantes de la carrera de Programacion que formaron
# sus grupos para elaborar el Laboratorio N°3. Los grupos son los siguientes:
# Grupo 1
# Marcos , Gabriela , Benjamin , Matias.
# Grupo 2
# Marcos , Nicolas , Diego , Matias.
# Se necesita saber si en ambos grupos tienen algun estudiante en comun y, en caso
# de que ası sea, imprimir los nombres de esos estudiantes. Todo esto utilizando sets.

grupo1 =set ({"Marcos", "Gabriela", "Benjamin", "Matias"})
grupo2 = set({"Marcos", "Nicolas", "Diego", "Matias"})
print(type(grupo1))
print(type(grupo2))
print(grupo1)
print(grupo2)

estcomun= grupo1.intersection(grupo2)
if len(estcomun)>0:
    print("los estudiantes que se repiten son: ", estcomun)

