suma = 0
while True:
    num = int(input('ingrese un numero (0 para terminar): '))
    if num == 0:
        break
    if num > 0:
        suma = suma + num 
print('la suma total es: ', suma)