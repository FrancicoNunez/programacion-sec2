

censo1 = {
    "Id" : 8 , 
    "Nombre" : "BioBio" , 
    "Superficie" : 23890 , 
    "Habitantes" : 1556805 , 
}
censo2 = {
     "id" : 10 , 
     "Nombre" : "los Lagos" ,
    "Superficie" : 48583 , 
    "Habitantes" : 828708 
}

habitantes1 = 1556805
habitantes2 = 828708
sup1= 23890
sup2= 48583
densidad = habitantes1/sup1
densidad2= habitantes2/sup2
print(censo1)
print(censo2)
censo2["densidad"] = round(densidad2,1)
censo1["densidad"]= round(densidad,1)
print("censo mas la densidad" , censo1)
print(censo2)
censo1["Capital"] = "concepcion"
censo2["Capital"] = "Puerto Montt"
censo1["Comunas"] = "Lota, Lebu, Los Ángeles"
censo2["Comunas"] = "Castro, Puerto Varas, Purranque"
censo1["Provincia"] = (" Osorno, Llanquihue, Chiloé , Palena")
censo2["Provincia"] = ("Osorno, Llanquihue,Chiloé,Palena")
print("nuevo censo actualizado" ,censo1)
print(censo2)
for clave , valor in censo1.items():
    print(clave, ":" , valor)
