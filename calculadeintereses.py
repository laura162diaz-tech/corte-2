import sys
print("digite la cantidad de dinero")
cantidaddinero = float(input('Introduce cantidaddinero: '))
print("digite el porcentaje del interes")
porcentajeinteres = float(input('Introduce porcentajeinteres: '))
print("digite el periodo")
periodo = float(input('Introduce periodo: '))
valorinteres = cantidaddinero*porcentajeinteres/100*periodo/360
valorimpuesto = valorinteres*0.07
neto = cantidaddinero+valorinteres-valorimpuesto
print("el valor de los intereses es", valorinteres)
print("su valor de impuestos es", valorimpuesto)
print("el valor a tetirar es", neto)


