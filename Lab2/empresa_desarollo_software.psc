Algoritmo empresa_desarollo_software
	Definir a, b Como Real
	Escribir " Hola, que servidor quiere ocupar? (1|2|3|4|5)"
	Escribir "1:norteamerica 2:centroamerica 3:sudamerica 4:europa 5:asiaoceania"
	leer a
	
	norteamerica<-0.02
	centroamerica<-0.03
	sudamerica<-0.05
	europa<-0.07
	asiaoceania<-0.09
	
	Segun a Hacer
		1:
			Escribir "eligio norteamerica"
			Escribir "cuantos gb desea almacenar?"
			leer b
			Repetir
				si b<0 Entonces
					Escribir "ingrese una cantidad de gb mayor a 0"
					leer b
				FinSi
			Hasta Que b>0
			Repetir
				si b>10000 Entonces
					Escribir "excede la capacidad maxima, se le cobrara un 20%"
					leer b
					Escribir "serian USD", norteamerica*b/0.8
				SiNo
					Escribir "ha selccionado" , b "(gb)"
					Escribir "serian USD", norteamerica*b
					
				FinSi
			Hasta Que b<10000
		2:
			Escribir "eligio centroamerica"
			Escribir "cuantos gb desea almacenar?"
			leer b
			Repetir
				si b<0 Entonces
					Escribir "ingrese una cantidad de gb mayor a 0"
					leer b
				FinSi
			Hasta Que b>0
			Repetir
				si b>10000 Entonces
					Escribir "excede la capacidad maxima,se le cobrara un 20%"
					leer b
					Escribir "serian USD", centroamerica*b/0.8
				SiNo
					escribir"ha selccionado" , b "(gb)"
					Escribir "serian USD", centroamerica*b
				FinSi
			Hasta Que b<10000
			
		3:
			Escribir "eligio sudamerica"
			Escribir "cuantos gb desea almacenar?"
			leer b
			Repetir
				si b<0 Entonces
					Escribir "ingrese una cantidad de gb mayor a 0"
					leer b
				FinSi
			Hasta Que b>0
			Repetir
				si b>10000 Entonces
					Escribir "excede la capacidad maxima, se le cobrara un 20%"
					leer b
					Escribir "serian USD", sudamerica*b/0.8
				SiNo
					Escribir "ha selccionado" , b "(gb)"
					Escribir "serian USD", sudamerica *b/0.8
				FinSi
			Hasta Que b<10000
			
		4:
			Escribir "eligio europa"
			Escribir "cuantos gb desea almacenar?"
			leer b
			Repetir
				si b<0 Entonces
					Escribir "ingrese una cantidad de gb mayor a 0"
					leer b
				FinSi
			Hasta Que b>0
				si b>10000 Entonces
					Escribir "excede la capacidad maxima, se le cobrara un 20%"
					Escribir "ha selccionado" , b "(gb)"
					Escribir "serian USD", europa*b/0.8
				SiNo
					Escribir "ha selccionado" , b "(gb)"
					Escribir "serian USD", europa*b
					
				FinSi
		
		5:
			Escribir "eligio asiaoceania"
			Escribir "cuantos gb desea almacenar?"
			leer b
			Repetir
				si b<0 Entonces
					Escribir "ingrese una cantidad de gb mayor a 0"
					leer b
				FinSi
			Hasta Que b>0
			Repetir
				si b>10000 Entonces
					Escribir "excede la capacidad maxima, se le cobrara un 20%"
					Escribir "ha selccionado" , b "(gb)"
					Escribir "serian USD", asiaoceania*b/0.8
				SiNo
					Escribir "ha selccionado" , b "(gb)"
					Escribir "serian USD", asiaoceania*b
				FinSi
			Hasta Que b<10000
			
		De Otro Modo:
			Escribir "porfavor seleccione uno de los mostrados arriba"
	Fin Segun
	

	
FinAlgoritmo
