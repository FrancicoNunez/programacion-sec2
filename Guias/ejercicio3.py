# Desarrollar un programa que al momento de ingresar los lados de un triangulo
# (a, b y c) en consola, indique si es equilatero, isosceles o escaleno. Tambien se
# solicita calcular el area utilizando la formula de Heron:

a = int(input("escriba el primer lado del triangulo : "))
b = int(input("escriba el segundo lado del triangulo : "))
c = int(input("escriba el tercer lado del triangulo : ")) 

perimetro = (a+b+c)/2
area = (perimetro*(perimetro-a)*(perimetro - b)*(perimetro - c))**(1/2)

if a==b and a==c and b==c :
    (print("el triangulo es equilatero y su area es ",area))
elif a!=b and b!=c and c!=a:
    (print("el triangulo es escaleno y su area es ",area))
else:
    a==b and c!=b 
    print("el triangulo es isosceles y su area es ",area)

