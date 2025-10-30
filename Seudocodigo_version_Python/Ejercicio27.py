'''
27. Ejercicio.
Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que
van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.
'''
nota = int(input("Introduce una nota (de 0 a 10) o -1 para terminar: "))
nota_De_10 = False
while nota != -1:
    if nota == 10:
        nota_De_10 = True
    nota = int(input("Introduce una nota (de 0 a 10) o -1 para terminar: "))

if nota_De_10:
    print("Hubo al menos una nota con valor 10.")
else:
    print("No hubo ninguna nota con valor 10.")
