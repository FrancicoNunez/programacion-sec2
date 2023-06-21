nombre = input("Ingrese el nombre del estudiante\n")
asignatura = input("Ingrese el nombre de la asignatura\n")
nota1 =float(input("Ingrese la nota de laboratorio 1\n"))
nota2 = float(input("Ingrese la nota de laboratorio 2\n"))
promedio = (nota1*0.3) + (nota2*0.7)
notas = {
    "nombre":nombre,
    "asignatura":asignatura,
    "Nota1":nota1,
    "Nota2":nota2,
    "promedio": round(promedio,1)
}
print(notas)
