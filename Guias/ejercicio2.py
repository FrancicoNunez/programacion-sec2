# Escribir un programa que pida al usuario ingresar dos palabras y las guarde en
# dos variables diferentes. Luego imprimir cual palabra tiene mas caracteres y cual
# tiene menos caracteres.

p1 = str(input("ingrese la primera palabra : "))
p2 = str(input("ingrese la segunda palabra : "))


print("la primera palabra tiene" , len(p1), "letras")
print("la segunda palabra tiene" ,len(p2), "letras") 
if p2>p1:
    print("la segunda palabra tiene mas letras")
else:
    print("la primera tiene mas letras")