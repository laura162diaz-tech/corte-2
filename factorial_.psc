Algoritmo factorial
	Definir num,factorial_,inferiores Como Entero
	Escribir "ingrese el numero para el factorial"
	Leer num
	si numero < 0 Entonces
		Escribir "no se puede calcular el factorial "
	SiNo
		factorial_ = 1
		inferiores= 1
		Repetir
			factorial_ = factorial_ * inferiores
			inferiores = inferiores + 1
			
		Hasta Que inferiores > num
		Escribir " factorial_ de  ", num ,"es:",factorial_
	FinSi
FinAlgoritmo
