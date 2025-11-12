a = float(input('ingresa el valor de a: '))
b = float(input('ingrese el valor de b: '))
c = float(input('ingrese el valor de c: '))
discriminante = b**2 - 4*a*c
print('el discriminante es: ', discriminante)
if a == 0:
    print('no tiene solucion(a no puede ser 0)')
elif discriminante >= 0:
    print('si tiene solucion')
else:
    print('no tiene solucion')
    
          
