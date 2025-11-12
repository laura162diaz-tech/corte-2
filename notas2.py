print('ingresa las 5 notas (0.0,5.0):')
nota1 = float(input('nota del trabajo 1: '))
nota2 = float(input('nota del trabajo 2: '))
nota3 = float(input('nota del trabajo 3: '))
nota4 = float(input('nota del trabajo 4: '))
nota5 = float(input('nota del trabajo 5: '))
suma = nota1 + nota2 + nota3 + nota4 + nota5
promedio = suma/5
print('tu nota final es:', promedio)
if promedio > 3.5:
    print('haz aprobado el curso')
else:
    print('haz reprobado el curso')
    

              