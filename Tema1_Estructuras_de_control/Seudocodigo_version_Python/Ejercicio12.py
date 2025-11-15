'''
12. Ejercicio.
Dibuja un ordinograma de un programa que muestre los números pares comprendidos
entre el 1 y el 200. Esta vez utiliza un contador sumando de 1 en 1
'''
cont = 1
while cont < 201:
    if cont % 2 == 0:
        print(cont)
    cont += 1
