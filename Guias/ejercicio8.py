# Elaborar un algoritmo que permita al usuario ingresar un mes y arroje la estacion
# correspondiente a ese mes: verano, otoño, invierno o primavera.

mes = input("ingrese un mes: ")
print()
estaciones = {
    "enero" : "verano",
    "febrero" : "verano", 
    "marzo" : "otoño", 
    "abril" : "otoño", 
    "junio" : "invierno", 
    "julio" : "invierno",
    "agosto" : "invierno",
    "septiembre" : "primavera",
    "octubre" : "primavera", 
    "noviembre" : "primavera", 
    "diciembre" : "verano"
}
if mes in estaciones:
    estacion = estaciones[mes]
    print(f"la estacion correspondiente al mes de {mes} es {estacion}")
    print("")
else:
    print("mes invalidado. Por favor, ingrese un mes valido en minusculas. ")