Algoritmo colun_yogurt
	
	definir a Como real	
	Escribir "Tenemos 10.000 unidades de yogur maqui el dia de hoy"
	Escribir "cuantos va a repartir?"
	leer a
	yogur<-10000
	resta<-10000-a
	Repetir
		si resta<0 Entonces
			Escribir "porfavor ingrese un valor mayor a 0"
		FinSi
	Hasta Que resta>0
	si resta=5000 Entonces
		Escribir "Precaución: el stock llego al 50% del total"
		Escribir "saco " , a " quedan " , resta " en stock"
	FinSi
	si resta<5000 Entonces
		Escribir "queda menos del 50% disponible"
		Escribir "saco " , a " quedan " , resta " en stock"
	FinSi
	si resta=3000 Entonces
		Escribir "El stock llego al 30% "
		Escribir "saco " , a " quedan " , resta " en stock"
	FinSi
	si resta<3000 Entonces
		Escribir "queda menos del 30% disponible "
		Escribir "saco " , a " quedan " , resta " en stock"
	FinSi
	si resta=1000 Entonces
		Escribir "Se llegó al stock critico, solo quedan 1000 unidades"
		Escribir "saco " , a " quedan " , resta " en stock"
	FinSi
	si resta<1000 Entonces
		Escribir "queda menos de 1000 unidades"
		Escribir "saco " , a " quedan " , resta " en stock"
	FinSi
	si resta=10000 Entonces
		Escribir "no queda mas stock para seguir repartiendo, saco todo el stock del dia de hoy"
	FinSi
	si resta>10000 Entonces
		Escribir "no se pueden sacar mas de 10000 unidades"
	FinSi
	
FinAlgoritmo
