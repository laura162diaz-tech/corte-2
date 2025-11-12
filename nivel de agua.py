litros = float(input('cuantos litros hay en el tanque'))
if litros < 250:
    print('abre la llave hay poca agua')
elif litros > 450:
    print('cierra la llave hay mucha agua')
else:
    print('nivel adecuado de agua')