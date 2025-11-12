costo = float(input('ingresa el valor del producto'))
if costo > 150000:
    print('aplica descuento del 5%')
    descuento = costo * 0.05
    total = costo - descuento
    print('descuento: $', descuento)
    print('total a pagar: $', total)
else:
    print('no aplica descuento')
    print('total a pagar: $', costo)
    