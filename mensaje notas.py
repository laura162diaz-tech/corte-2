num = float(input('ingrese el valor de su nota'))
if num < 3.0:
    print('insuficiente')
elif num <= 3.5:
    print('aceptable')
elif num <= 4.0:
    print('sobresaliente')
else:
    print('exelente')