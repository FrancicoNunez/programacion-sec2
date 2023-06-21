Algoritmo Circo_de_osorno
	
	Escribir "entrada general es de 5000$ si tiene niño o adultos mayores hay descuento"
	Escribir "niños menores de 12 años tienen un descuento de un 30%"
	Escribir "adultos mayores de 65 años tienen un descuento de un 25%"
	Escribir "ademas si compra mas de 2 entradas tendra un descuento de 10% adicional"
	Escribir "¿cuantos años tiene?"
	leer num1
	si num1<12 Entonces
		escribir "tiene un 30% de descuento"
		
	FinSi
	si num1>12 Entonces
		Escribir "no tiene descuento"
		
	FinSi
	
	si num1<65 entonces 
		escribir "no tiene descuento"
		
	FinSi
	si num1>65 Entonces
		Escribir "tiene un 25% de descuento"
		
	FinSi
Escribir "¿cuantas entradas desea comprar?"
leer num2 
si num2<2 Entonces
	Escribir "no tiene descuentos adicionales"
FinSi

si num2>3  Entonces
	Escribir "tiene un 10% de descuento adicional"
	
FinSi

FinAlgoritmo
