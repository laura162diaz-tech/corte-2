while True:
    print('1. sumar')
    print('2. restar')
    print('3, salir')
    opcion = input('seleccione una opcion: ')
    if opcion == '1':
        num1 = float(input('primer numero: '))
        num2 = float(input('segundo numero: '))
        resultado = num1 + num2
        print('resultado: ', resultado)
    elif opcion == '2':
        num1 = float(input('primer numero: '))
        num2 = float(input('segundo numero: '))
        resultado = num1 - num2
        print('resultado: ', resultado)
    elif opcion == '3':
        print('adios')
        break
    else:
        print('opcion incorrecta')
        
