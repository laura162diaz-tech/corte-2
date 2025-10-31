Algoritmo  EncuestaPlataforma
		Definir codigo, plataforma Como Cadena
		Definir n, i Como Entero
		Definir votosAndroid, votosIOS Como Entero
		votosAndroid = 0
		votosIOS = 0
		
		Escribir "¿Cuantos estudiantes van a votar?"
		Leer n
		
		Para i = 1 Hasta n Con Paso 1 Hacer
			Escribir "Ingrese el codigo del estudiante ", i, ":"
			Leer codigo
			
			Escribir "Ingrese su plataforma preferida (Android / iOS):"
			Leer plataforma
			
			Si Mayusculas(plataforma) = "ANDROID" Entonces
				votosAndroid = votosAndroid + 1
			Sino
				Si Mayusculas(plataforma) = "IOS" Entonces
					votosIOS = votosIOS + 1
				Sino
					Escribir "Plataforma no valida. Voto no contabilizado."
				FinSi
			FinSi
		FinPara
		
		Escribir ""
		Escribir "Resultados de la encuesta:"
		Escribir "Votos Android: ", votosAndroid
		Escribir "Votos iOS: ", votosIOS
		
		Si votosAndroid > votosIOS Entonces
			Escribir "La plataforma elegida es: ANDROID"
		Sino
			Si votosIOS > votosAndroid Entonces
				Escribir "La plataforma elegida es: iOS"
			Sino
				Escribir "Hay un empate. Se requiere otro mecanismo de eleccion."
			FinSi
		FinSi
FinAlgoritmo

	
