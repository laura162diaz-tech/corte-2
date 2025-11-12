num = int(input('ingrese un numero: '))
while num >= 0:
    if num % 7 == 0 and num != 0:
        print(num, '¡alerta! multiplo de 7 ')
    else:
        print(num)
    num = num - 1