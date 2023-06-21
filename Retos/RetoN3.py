ciudades = ["santiago", "temuco", "osorno", "punta arenas"]
indice = [134 , 99, 245, 50]
Ciudad_ICA = list(zip(ciudades,indice))
print(Ciudad_ICA)
print("")

print( f"la ciudad de {ciudades[3]} es la ciudad con el indice de calidad de aire mas bajo, y es de  {indice[3]}")
print(f"la ciudad de {ciudades[2]} es la ciudad con el indice de calidad de aire mas alto, y es de  {indice[2]}")
print("")
print( "ICA = 0-50(Buena), 51-100(Moderada), 101-150(Dañina a la salud para grupos sensibles), 201-200(Muy dañina a la salud)")
print("")
print(f"{ciudades[0]} tiene un ica de : {indice[0]} , la cual es Dañina a la salud para grupos senisbles" )
print(f"{ciudades[1]} tiene un ica de : {indice[1]} , lo cual es Moderada")
print(f"{ciudades[2]} tiene un ica de : {indice[2]} , lo cual es Muy dañina a la salud")
print(f"{ciudades[3]} tiene un ica de : {indice[3]} , la cual es Buena")



