minimo = int(input('ingrese el valor minimo del intervalo'))
maximo = int(input('ingrese el valor maximo del intervalo'))
numero = int(input('ingrese el numero a verficar'))
if numero >= minimo and numero <= maximo:
    print('el numero', numero, 'esta dentro del intervalo')
else:
    print('el numero', numero, 'esta fuera del intervalo')
    
             