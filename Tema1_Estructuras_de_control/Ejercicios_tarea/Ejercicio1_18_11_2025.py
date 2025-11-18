'''
        *
      * *
     *  *
    *   *
   *    *
  *     *
   *    *
    *   *
     *  *
      * *
        *
'''
altura = int(input("Introduce la altura de la escalera: "))
for i in range(altura):
    linea = " " * (altura - i - 1) + "*" 
    if i > 0: 
        linea += " " * (i - 1) + "*"
    print(linea) 
for i in range(altura - 2, -1, -1):
    linea = " " * (altura - i - 1) + "*"
    if i > 0:
        linea += " " * (i - 1) + "*"
    print(linea)  