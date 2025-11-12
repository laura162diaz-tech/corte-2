n1 = int(input('ingrese el primer numero'))
n2 = int(input('ingrese el segundo numero'))
n3 = int(input('ingrese el tercer numero'))
n4 = int(input('ingrese el ultimo numero'))
mayor = n1 
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
if n4 > mayor:
    mayor = n4
print('el numero mayor es: ', mayor)