# operadores aritmeticos
a =1
b =3
print("suma entre a + b es : ", a + b )
print("resta entre a - b es : ", a - b)

t = 5.39
g = 9.81

v = g * t 
print( f" la velocidad del objeto en caida libre es {v:.2f}")

c2 = complex(3, -5)
print ("el numero completo es ",c2)
print(c2.real)
print(c2.imag)

print("hola" * 5)
print("hola" * (int((10*2) / 5 )))

#operador de comparacion 
print(a == b)
print (a != b)
print (a > b)
print (a < b)
print (a >= b)
print (a <= b)

animal_domestico = "gato"
animal_salvaje = "leopardo"
print(animal_domestico == animal_salvaje)
print(animal_salvaje != animal_domestico)
#tabla asci
print(animal_domestico > animal_salvaje)

#operadores logicos
bencina = True
encendido = True
edad = 19
if bencina and encendido:
    print("el vehiculo puede avanzar")
else :
    print("el vehiculo no puede avanzar")

if bencina or encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede avanzar")

if not bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede avanzar")
if not bencina or encendido:
    print("utilizando NOT y OR : el vehiculo puede avanzar")
else: 
    print("el vehiculo no puede avanzar")

if not bencina or (encendido and edad >= 18): #and y falso = false// or y falso = true
    print("el vehiculo puede avanzar")
else :
    print("el vehiculo no puede avanzar")
    

edad = 19
if edad >= 18:
    print("usted es mayor de edad")
else: print("usted es menor de edad")

edad =66
if edad>= 18 and edad< 65:
    print("eres mayor de edad")
elif edad>= 65:
    print("eres un adulto mayor")
else: print("eres menor de edad")

#operador ternario
edad = 19
print("usted puede votar" if edad>= 18 else "usted no puede votar")