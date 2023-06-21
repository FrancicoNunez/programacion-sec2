Algoritmo numero_mayor_entre_3
	Escribir "Ingrese el primer numero ",num1
	Leer num1
	Escribir "Ingrese el segundo numero ", num2
	Leer num2
	Escribir "Ingrese el tercer numero  ", num3
	Leer num3
	
	si num1>num2 y num1>num3 Entonces
		Escribir "el numero mayor es ",num1
	FinSi
	
	si num3>num2 y num3>num1 Entonces
		Escribir "el numero mayor es ",num3
	FinSi
	
	si num2>num1 y num2>num3 Entonces
		Escribir "el numero mayor es ",num2
	FinSi
FinAlgoritmo
