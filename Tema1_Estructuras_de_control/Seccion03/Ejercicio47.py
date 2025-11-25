'''
47. Ejercicio. 
Escribe  un  programa  que  diga  si  un  número  introducido  por  teclado  es  o  no  primo.  Un 
número  primo  es  aquel  que  sólo  es  divisible  entre  él  mismo  y  la  unidad.  Nota:  Es  suficiente 
probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.
'''
import math
num = int(input("Dime un numero y te dire si es primo o no: "))
es_primo = True
if num < 2:
    es_primo = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            es_primo = False
            break
if es_primo:
    print(f"El numero {num} es primo.")
else:
    print(f"El numero {num} no es primo.")
    
    