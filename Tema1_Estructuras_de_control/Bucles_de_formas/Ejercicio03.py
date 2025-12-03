'''
Ejercicio 3: Pirámide con huecos internos (estructura tipo "reja")
Enunciado:

Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.

Figura para n=6:

     *
    * *
   *   *
  * * * *
 *       *
***********
'''


'''
n = int(input("Introduce la altura de la pirámide (n): "))
for altura in range(n):
    linea = ""
    for anchura in range(n):
        if anchura == n and altura == 0 or  n - anchura :
            linea += "*"
        else:
            linea += " "
    print(linea)
'''
altura = int(input("Dime la altura de la pirámide: "))

for i in range(1, altura + 1):
    espacios = altura - i

    if i == 1:
        print(" " * espacios + "*")
    elif i == (altura // 2)+1 :
        print(" "*(altura-i)+"* " * ((altura//2)+1))
    elif i == altura:
        print("*" * ((altura *2 )-1))
    else:
        print(" " *espacios + "*" + " " *(2 * i - 3) + "*")