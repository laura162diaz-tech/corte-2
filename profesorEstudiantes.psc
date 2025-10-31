Algoritmo profesorEstudiantes
	Definir notaDefinitiva, sumaDefinitivas, promediogrupos Como Real
	Definir cantidadEstudiantes,contadorEstudiantes,aprobaron , reprobaron Como Entero
	Definir codigoEstudiante como cadena  
	Escribir " ingrese la cantidad estudiantes "
	Leer cantidadEstudiantes
	Mientras contadorEstudiantes<cantidadEstudiantes
		Escribir "ingrese el codigo del estudiante"
		Leer codigoEstudiante
		Escribir "ingrese la nota definitiva:"
		Leer notaDefinitiva
		si notaDefinitiva >= 3.0 Entonces
			aprobaron=aprobaron+1 
		SiNo
			reprobaron= reprobaron+1 
		FinSi
		sumaDefinitivas= sumaDefinitivas + notaDefinitiva
		contadorEstudiantes = contadorEstudiantes + 1
		
	
	FinMientras 
	promediogrupos = sumaDefinitivas/cantidadEstudiantes
	Escribir " la cantidad de estudiantes que aprobaron es:" aprobaron
	Escribir "la cantidad de estudiantes que reprobaron es :" reprobaron
	Escribir "el promedio es:" promediogrupos
FinAlgoritmo
