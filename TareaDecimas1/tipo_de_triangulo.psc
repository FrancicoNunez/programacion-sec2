Algoritmo tipo_de_triangulo
	definir num1, num2, num3 Como real
	
	Escribir " Escriba los 3 lados del triangulo"
	Leer num1, num2, num3
	perimetro<- num1+num2+num3
	s=perimetro/2
	area<- raiz(s*(s-num1)*(s-num2)*(s-num3)) 

	si num1 == num2 y num1 == num3 y num2 == num3 Entonces
		
		Escribir "el triangulo es equilatero"
		
	FinSi
	si (num1 == num2) y (num2<>num3) Entonces
		Escribir "El triangulo es Isosceles"
	FinSi
	si num1<> num2 y mum1 <> num3 y num2 <> num3 Entonces
		Escribir " El tringulo es escaleno"
	FinSi
	Escribir "su perimetro es " ,perimetro
	Escribir " Su area es " ,area
	
FinAlgoritmo
