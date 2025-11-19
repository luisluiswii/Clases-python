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
altura = int(input("Dime la altura: "))

print(" " * (altura - 1) + "*") 
for i in range(1, altura):
    espacios_externos = " " * (altura - i - 1)
    espacios_internos = " " * (2 * i - 1)
    print(espacios_externos + "*" + espacios_internos + "*")

for i in range(altura - 1, -1, -1):
    if i == 0:
        print(" " * (altura - 1) + "*")
    else:
        espacios_externos = " " * (altura - i - 1)
        espacios_internos = " " * (2 * i - 1)
        print(espacios_externos + "*" + espacios_internos + "*")
