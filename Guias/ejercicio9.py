# Se tiene la siguiente lista de enteros:
# numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
# Se solicita:
# a) Eliminar el ´ultimo elemento de la lista
# b) Agregar en la primera posici´on el n´umero 2
# c) Eliminar los n´umeros duplicados de la lista
# d) Obtener la media y la mediana de la lista

numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
print(type(numeros))
print(numeros)
del numeros[8]
print("eliminando el ultimo numero", numeros)
numeros.insert(0,2)
print("agregado el numero 2 al inicio" ,numeros)
del numeros[2]
del numeros[7]
print("sin numeros duplicados" ,numeros)
import statistics
print("la media de la lista es" , statistics.mean(numeros))
print("la mediana de la lista es" , statistics.median(numeros))

