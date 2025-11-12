numero = int(input('ingrese el numera a verificar: '))
print('primer intervalo: ')
min1 = int(input('limite minimo del intervalo: '))
max1 = int(input('limite maximo del intervalo: '))
print('segundo intervalo: ')
min2 = int(input('limite minimo del intervalo: '))
max2 = int(input('limite maximo del intervalo: '))
print('tercer intervalo: ')
min3 = int(input('limite minimo del intervalo: '))
max3 = int(input('limite maximo del intervalo: '))
intervalo1 = numero > min1 and numero < max1
intervalo2 = numero > min2 and numero < max2
intervalo3 = numero > min3 and numero < max3
if intervalo1:
    print('el numero', numero, 'esta dentro del primer intervalo')
elif intervalo2:
    print('el numero', numero, 'esta dentro del segundo intervalo')
elif intervalo3:
    print('el numero', numero, 'esta dentro del tercer intervalo')
else:
    print('el numero', numero, 'esta fuera de todos los intervalos')
    
