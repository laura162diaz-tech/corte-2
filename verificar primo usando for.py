num = int(input('ingrese un numero entero mayor que 1: '))
primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo:
    print('el numero es primo')
else:
    print('no es primo')
    