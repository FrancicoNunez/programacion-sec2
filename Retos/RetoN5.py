print()
n1 = int(input("ingrese el primer numero: "))

if n1 % 2 == 0 :
    print(f"el numero, que es: {n1}. Es par")
else: print(f"el numero, que es : {n1}. Es inpar")
valor = range(2,n1)
contador = 0
for n in valor:
    if n1 % n == 0:
        contador +=1
        print("los divisores son : ",n)
if contador > 0 :
    print(f"el numero {n1}, no es primo")
else: print(f"el numero {n1}, es primo")
while n1 >= 50 :
    print(f"el numero, que es: {n1}. Es mayor a 50")
    break
else: print(f"el numero, que es: {n1}. Es menor a 50")
