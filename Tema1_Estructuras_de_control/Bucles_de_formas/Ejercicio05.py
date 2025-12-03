'''
Ejercicio 5: Cruz con borde punteado
Enunciado:

Imprime una cruz en una matriz de tamaño n x n con puntos en el borde, asteriscos en las líneas vertical y horizontal centrales, y espacios en el resto.

Figura para n=7:

. . . . . . .
. * . * . * .
. . * . * . .
* * * * * * *
. . * . * . .
. * . * . * .
. . . . . . .
'''
altura =  int(input("Dime la altura de la figura, debe ser un numero impar: "))

for i in range (altura):
    if i == 0 or i == altura-1:
        print("."*altura)
    if altura == 2 //altura:
        print("*"* altura)
    else:
        print(".")







