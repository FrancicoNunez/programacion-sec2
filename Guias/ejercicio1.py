# Realizar un algoritmo que indique el numero menor y el numero mayor entre tres
# enteros leidos por consola. Solo se deben ingresar numeros enteros.
n1 = int(input("ingrese el primer numero : "))
n2 = int(input("ingrese el segundo numero : "))
n3 = int(input("ingrese el tercer numero : "))

if n1>n2 and n2>n3  :
  print( n3, n2, n1)
elif n2>n1 and n1>n3 :
  print(n3 , n1 , n2)
else:
  n3>n2 and n2<n1
  print(n2 , n1, n3)
