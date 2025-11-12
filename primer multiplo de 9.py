n = int(input('ingrese el primer numero: '))
m = int(input('ingrese el segundo numero: '))
encontrado = False
for i in range(n, m + 1):
    if i % 9 == 0:
        print('primer multiplo de 9: ', i)
        encontrado = True
        break
if not encontrado:
    print('no hay multiplo de 9')
    