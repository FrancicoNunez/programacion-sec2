peso = 65
estatura = 1.70
print(f"mi peso es {peso}(kg) y mi estatura es {estatura}(m)")

imc = peso / (estatura**2)
print("mi imc es", imc)

print("mi peso en real es",float(peso))
print("mi peso es entero es",int(peso))
print("mi imc es:{:.2f}".format(imc))

universidad = "universidad de los lagos"
carrera = "ingenieria civil en informatica"
clase = "programacion"
print("la cantidad de caracteres en universidad son ",len(universidad) )
print("la cantidad de caracteres en carrera son",len(carrera))
print("la cantidad de caracteres en clase son",len(clase))

ampolleta = False
interruptor = True
print(bool(0))
print(bool(1))
print(bool(ampolleta))
print(bool(interruptor))

estudiantes=["nuñez", "kevin", "leandro", "nacho","nuñez"]
num=[17, 12, 21, 10, 17]
lenguaje=["python"]
listamixta=[17, "nuñez" ,True]
print("los jugadores de hoy son" ,estudiantes)
print("los numeros de los jugadores son",num)
print("el lenguaje con el que trabajaremos sera",lenguaje)
print("el primer jugador es",listamixta)
print(len(listamixta))
print(estudiantes.count("nuñez"))
print(num.count(17))
print(estudiantes[1])
print(estudiantes[-2])
