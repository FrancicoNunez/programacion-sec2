
nota1 = float(input("ingrese la nota: "))
nota2 = float(input("ingrese la nota: "))
nota3 = float(input("ingrese la nota: "))
nota4 = float(input("ingrese la nota: "))
nota5 = float(input("ingrese la nota: "))
nota6 = float(input("ingrese la nota: "))
nota7 = float(input("ingrese la nota: "))
nota8 = float(input("ingrese la nota: "))
nota9 = float(input("ingrese la nota: "))
nota10 = float(input("ingrese la nota: "))

notas = [nota1, nota2, nota3, nota4, nota5,nota6,nota7,nota8,nota9,nota10]
print(notas)
import statistics
print("la media de calificaciones en programacion es de :  ", statistics.mean(notas))





newlista = notas
for i in newlista:
    print(i)
print()