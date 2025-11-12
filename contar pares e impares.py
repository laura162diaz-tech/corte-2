pares = 0
impares = 0
while True:
    num = int(input('ingrese un numero (0 para terminar): '))
    if num == 0:
        break
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1 
print('pares: ', pares)
print('impares: ', impares)