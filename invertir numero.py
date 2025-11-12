num = int(input('ingrese un numero de dos cifras o mas: '))
invertido = 0
while num > 0:
    ultimoDigito = num % 10
    invertido = invertido * 10 + ultimoDigito
    num = num // 10
print('numero invertido: ', invertido)