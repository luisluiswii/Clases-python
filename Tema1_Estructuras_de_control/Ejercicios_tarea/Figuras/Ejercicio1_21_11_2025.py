'''
Ejercicio 8: Rombo sólido
Enunciado:

Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.

Figura para n=4:
   *
  ***
 *****
*******
 *****
  ***
   *
   
'''

largo = int(input("Dime el alto de la piramide que quieras: "))

for i in range(largo):
    print(" " * (largo - i - 1) + "*" * (2 * i + 1))

for i in range(largo - 2, -1, -1):
    print(" " * (largo - i - 1) + "*" * (2 * i + 1))