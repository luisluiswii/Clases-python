'''
28. Ejercicio.
Dibuja un ordinograma de un programa que suma independientemente los pares y los
impares de los números comprendidos entre 100 y 200, y luego muestre por pantalla ambas
sumas.
'''
num_Par = 0
num_Impar = 0
for i in range(100, 201):
    if i % 2 == 0:
        num_Par += i
    else:
        num_Impar += i
print("La suma de los números pares entre 100 y 200 es:", num_Par)
print("La suma de los números impares entre 100 y 200 es:", num_Impar)
