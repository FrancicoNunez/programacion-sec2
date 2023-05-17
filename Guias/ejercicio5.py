# Crear un algoritmo que solicite por consola las 3 notas de los laboratorios realizados en el ramo de 
# Programacion. Luego obtener el promedio ponderado de la siguiente manera:
# Promedio Ponderado = Lab1 * 0,3 + Lab2 * 0,4 + Lab3 * 0,3
# Si el promedio es menor a 4,0 debe imprimir el mensaje que el estudiante reprobo
# la asignatura. Si el promedio es superior a 4,0, indicar que el estudiante aprobo
# la asignatura. Si la nota es superior 6,0, debe mostrar el mensaje: el estudiante aprobo con distincion.

n1 = float(input("ingrese la primera nota de laboratorio :  "))
n2 =float(input("ingrese la segunda nota de laboratorio :  "))
n3 = float(input("ingrese la tercera nota de laboratorio :  "))
promedio_ponderado = n1*0.3 + n2*0.4 + n3*0.3
print("el promedio del estudiante es", round(promedio_ponderado,1))

if promedio_ponderado>=1.0 and promedio_ponderado < 4.0:
    print("el estudiante reprobo la asignatura")
elif promedio_ponderado>4.0 and promedio_ponderado < 6.0:
        print("el estudiante aprobo la asignatura")
else: promedio_ponderado>6.0 
print("el estudiante aprobo con distincion ")