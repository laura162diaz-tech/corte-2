print("digite su salario")
salario = float(input('Introduce salario: '))
valorimpuestos = salario*8/100
neto = salario-valorimpuestos
print("el valor del impuesto es", valorimpuestos)
print("y su salario es", neto)
