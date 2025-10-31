Algoritmo sistemaDecimal
	definir cifra, num,contador,sumacifras,mods,sumamods Como Entero
	Escribir " ingrese una cifra:"
	Leer cifra 
	num = 10
	Mientras mods <> cifra y cifra <>0 Hacer
		mods=cifra MOD num
		contador=contador+1
		cifra = trunc(cifra/num)
		sumamods=sumamods + mods
		Escribir mods
	FinMientras
	Escribir " contador:",contador;
	Escribir sumamods
FinAlgoritmo
