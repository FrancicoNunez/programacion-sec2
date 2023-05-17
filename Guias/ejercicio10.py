# . Crear una agenda telefonica que contenga un solo contacto. Esta agenda se debe
# guardar en un diccionario. Este diccionario debe contar con las siguientes claves:
# Nombre
# Direccion
# Ciudad
# Numero telef´onico
# A continuaci´on, agrega una nueva clave llamada “Redes Sociales” que contenga al
# menos tres nombres de perfil de diferentes redes sociales (por ejemplo, Facebook,
# Instagram y Twitter). Por ´ultimo, se solicita imprimir solamente el Facebook del
# contacto y luego la agenda completa actualizada.

Agenda_telefonica = {
    "Nombre" : "poch" , 
    "Direccion" : "Calle petritxol" ,
    "Ciudad" : "Barcelona" , 
    "Numero Telefonico" :"+3412345678"
}
print("los datos del contacto son los siguientes : \n" , Agenda_telefonica)
print("")

Agenda_telefonica ["Redes Sociales"] = "FACEBOOK: joan poch " , "INSTAGRAM : Joanpochhh_" , "TWITTER : joanpoch "

print("Aqui esta la red social de" ,Agenda_telefonica["Redes Sociales"][0])
print("")

print("agenda actualizada con las redes sociales del contacto \n" , Agenda_telefonica)