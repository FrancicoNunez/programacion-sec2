#01-Declarar una funcion simple
def mi_primer_funcion():
    print("esta es mi primera funcion")

mi_primer_funcion()

#02-Declarando una funcion y utilizando listas
def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar()
print(concatenar(lista1,lista2))
#03-Declarando una funcion multiplicacion pasando parametros
def multiplicacion(num1,num2):
    return num1*num2
#multiplicacion()
print(multiplicacion(10,2))
#04-Funciones suma y resta (por teclado)
def suma(a,b):
    return a+ b
def resta(a, b):
    return a - b
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
#Se llama a la funcion suma
resultado = suma(a,b)
print("La suma es de: ",resultado)
#Se llama a la funcion resta
resultado2 = resta(a,b)
print("La resta es de: ",resultado2)
def saludo(nombre):
    print("hola, mi nombre es " + (nombre))
saludo("tomas")
