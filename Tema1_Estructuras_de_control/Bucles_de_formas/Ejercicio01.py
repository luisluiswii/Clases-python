'''
Ejercicio 1: Diamante hueco
Enunciado:

Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.

Figura para n=5:

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''
alto = int(input("Introduce la altura del diamante (n): "))
print(" " * alto + "*")
for i in range(1, alto+1):
    linea = " " *(alto-i)+ "*"+ " " * (2* i-1) + "*"
    print(linea)
for i in range(1, alto):
    linea = " " * i + "*" + " " * (2*(alto-i)-1) + "*"
    print(linea)
print(" " * alto + "*")