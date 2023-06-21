def Bisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 400 != 0:
        return True
    elif año % 100 != 0:
        return True
    else:
        return True


año = int(input("Ingrese un año: "))

if Bisiesto(año):
    print("El año", año, "si es bisiesto")

else:
    print("El año", año, "no es bisiesto")
