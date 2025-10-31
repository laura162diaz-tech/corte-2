Algoritmo repasarTabla
	Definir tabla ,respuesta,aciertos, i ,resultado Como Entero
	Definir continuar Como Caracter
	Repetir
	aciertos = 0
	Escribir "que tabla deseas repasar del (1 al 20 )"
	Leer tabla 
	para i = 1 Hasta 10 Con Paso 1 Hacer
		Escribir " ¿cuanto es ",tabla,"x",i,"?"
		Leer  respuesta
		resultado = tabla * i
		si respuesta = resultado Entonces
			Escribir "Felicitaciones :)"
			aciertos = aciertos + 1
		SiNo
			Escribir "incorrecto :(.la respuesta correcta es =", resultado 
		finsi	
	FinPara
	Escribir " total aciertos:",aciertos
	si aciertos <= 5 Entonces
		Escribir "su valoracion es:Insuficiente "
	SiNo
		si aciertos <= 7 Entonces
			Escribir "su valoracion es:Aceptable "
		SiNo
			si aciertos <= 9 Entonces
				Escribir "su valoracion es:Sobresaliente "
			SiNo
				si aciertos =10 Entonces
					Escribir "su valoracion es:Excelente"
				FinSi
			FinSi
		FinSi
	FinSi
	Escribir " "
	Escribir "¿Quieres repasar otra tabla? si/no "
	Leer continuar
	
Mientras Que continuar = "si"
FinAlgoritmo
