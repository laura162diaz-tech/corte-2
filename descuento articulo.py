tipo = int(input('ingrese el tipo de articulo (1,2,3)'))
if tipo == 1:
    descuento = 12.5
elif tipo == 2:
    descuento = 8.3
elif tipo == 3:
    descuento = 3.2
else:
    descuento = 0.0
print('descuento aplicado:', descuento, '%')