claveCorrecta = '1234'
intentos = 0
while intentos < 3:
    clave = input('ingrese la clave: ')
    if clave == claveCorrecta:
        print('acceso permitido')
        break
    else:
        intentos = intentos + 1
        print('clave incorrecta')
if intentos == 3:
    print('acceso denegado')