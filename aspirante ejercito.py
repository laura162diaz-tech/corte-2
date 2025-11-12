genero = input('ingrese genero (mujer/hombre)')
estatura = float(input('ingrese su estatura en metros:'))
edad = int(input('ingrese su edad'))
estadoCivil = input('ingrese su estado civil')
if estadoCivil == 'soltero':
    if genero == 'mujer':
        if estatura > 1.60 and edad >= 20 and edad <= 25:
            print('apta para ingresar en el ejercito')
        else:
            print('no apta para ingresar al ejercito')
    elif genero == 'hombre':
        if estatura > 1.65 and edad >= 18 and edad <= 24:
            print('apto para ingresar al ejercito')
        else:
            print('no apto para el ejercito')
    else:
        print('genero no valido')
else:
    print('debe ser soltero')