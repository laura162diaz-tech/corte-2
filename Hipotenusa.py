import math
raiz = math.sqrt
print("introduce el primer cateto:")
cateto1 = float(input('Introduce cateto1: '))
print("introduce el segundo cateto:")
cateto2 = float(input('Introduce cateto2: '))
hipotenusas = raiz(cateto1**2 + cateto2**2)
print("la hipotenusa del triángulo es ", hipotenusas)
