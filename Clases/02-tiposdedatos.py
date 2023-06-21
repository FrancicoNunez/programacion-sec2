peso = 65
estatura = 1.70
print(f"mi peso es {peso}(kg) y mi estatura es {estatura}(m)")

imc = peso / (estatura**2)
print("mi imc es", imc)
#float,int
print("mi peso en real es",float(peso))
print("mi peso es entero es",int(peso))
print("mi imc es:{:.2f}".format(imc))
#Len
universidad = "universidad de los lagos"
carrera = "ingenieria civil en informatica"
clase = "programacion"
print("la cantidad de caracteres en universidad son ",len(universidad) )
print("la cantidad de caracteres en carrera son",len(carrera))
print("la cantidad de caracteres en clase son",len(clase))
#bool
ampolleta = False
interruptor = True
print(bool(0))
print(bool(1))
print(bool(ampolleta))
print(bool(interruptor))
#LISTAS[]
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
print("suma de listas",estudiantes + num)
print( list(range(0,9)))
#tupla()
grupo1 = ("francisco", "felipe", "marilyn", "santiago" , 17, 3, 24)
print(type(grupo1)) #para ver que tipo es
print("los grupos son" ,grupo1)

list=(grupo1)

#Set{}
conjunto_colores=set({"rojo","negro", "azul"})
conjunto_animales=set({"perro", "gato", "pajaro"})
print(type(conjunto_animales))
conjunto_animales.add("loro")
print("el set de colores es", conjunto_colores)
print("el set de animales es",conjunto_animales)
conjunto_colores.add("rosa")
print("el nuevo set de colores es",conjunto_colores)

#Diccionarios dict{}
datos_personales = {
    "nombre":"Francisco",
    "Institucion":"Ulagos",
    "edad": 18,
    "Asignaturas": {"estructura de datos", "programacion"} 
}
print("diccionario inicial:" ,datos_personales)
datos_personales ["ciudad"] = "Osorno"
print("nuevo", datos_personales)
del(datos_personales)["ciudad"]
print("nuevos datos actualizados",datos_personales)
# miercoles tuplas set listas y diccionarios ejercicio 9 y 10

