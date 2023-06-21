def vuelto_producto(monto,pago):
    billetes=[20000,10000,5000,2000,1000,500,100,10,5,1]
    desglose={}
    vuelto=pago-monto
    for billete in billetes:
        if vuelto>=billete:
         cantidad=vuelto//billete
         desglose[billete]=cantidad
         vuelto-=cantidad*billete
        
    return desglose

precio = int(input("Cuanto cuesta lo que desea comprar?: "))

if precio :
   pagorealizado=int(input("¿con cuanto desea pagar?: "))
   
   resultado=vuelto_producto(precio,pagorealizado)
   if pagorealizado>precio:
      print(f"su vuelto en billetes y monedas es {resultado}")
   elif pagorealizado<precio:
      print("ingrese un valor valido")
