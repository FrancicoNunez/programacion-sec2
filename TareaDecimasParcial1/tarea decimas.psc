Algoritmo sin_titulo
    definir n1,n2,n3,n4,n5,menu Como entero
    Escribir "Bienvenido!el menu del dia de hoy es: "
    Escribir "1. papas fritas chicas $1500"
    Escribir "2. completo italiano $2000"
    Escribir "3. vaso de bebida 500ml $800"
    Escribir "4. empanada de carne $2500"
    Escribir "5. sandwich de jamon y queso $1000"
    Escribir "seleccione un numero del menu"
    Leer menu
    n1<-1500
    n2<-2000
    n3<-800
    n4<-2500
    n5<-1000
    Segun menu Hacer
        1:
            menu<-1500
            iva<-n1*0.19
        2:
            menu<-2000
            iva<-n2*0.19
        3:
            menu<-800
            iva<-n3*0.19
        4:
            menu<-2500
            iva<-n4*0.19
        5:
            menu<-1000
            iva<-n5*0.19
        De Otro Modo:
            Escribir "el numero de menu no existe"
    Fin Segun
    Escribir "el total de su compra es: $",menu
    Escribir "y el iva es: ",iva
FinAlgoritmo
