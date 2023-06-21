edad = 15
num = 0
"""while edad <18:
    print("eres menor de edad")"""

#bucle infinito
"""while True:
    print(num)
    num +=2"""

#While(Mientras)
num = 0
while num<= 100:
    print(num)
    num += 2

#Break
"""while True:
    parametro = input(">")
    if parametro == "exit":
        break
    else: print(parametro)"""""

#While(else/if)
while num<= 100:
    print(num)
    num +=2
else: print("mi condicion es igual o mayor a 100")
while num<= 200:
    print(num)
    num +=2
else: print("mi condicion es igual o mayor a 200")
while num <= 300:
    print(num)
    num += 2
    if num == 250: 
        print("mi condicion es igual a 250")
print("el tercer bucle se termino")

#While/break
while num <= 400:
    print(num)
    num+=2
    if num ==350:
        print("se detiene la ejecucion")
        break   
print(num)
print("el cuarto bucle se termino")


# loop infinito + break
while True:
    parametro = input("<")
    if parametro == "exit":
        break
    else:
        print(parametro)
#ordenar numeros en forma vertical
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)
#no esta bien optimizado
print()
print("for n2 \n")

newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)
print()
print("for n3 \n")
for i in range(1,11):
    print(i)