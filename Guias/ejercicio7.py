# Crear una lista con nombres de 5 trabajadores y otra lista con las edades de
# estos 5 trabajadores, Se solicita relacionar ambas listas en una sola estructura.
# La salida puede ser en tuplas o en un diccionario.

trabajadores = ("Michael Jackson", "Haaland", "Neymar", "Messi", "Mbappe")
Edades = (27 , 20, 33 , 36, 18)
total = tuple(zip(trabajadores, Edades))

print(total)
print(type(total))

