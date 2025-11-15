'''
9.  Ejercicio. 
Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego 
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.
'''
cont = 0
contPositivo = 0
contNegativo = 0

while num == 0:
    num= int(input("Dime un numero no nulo: "))
    if num == 0:
        print("numero no valido")
        continue
    if num < 0:
        print("numero negativo")
        contNegativo += 1
    else:
        contPositivo +=1
    cont += 1
print("Hubieron positivos: ", contPositivo, " y negativos: ", contNegativo)    