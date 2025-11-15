'''
8.  Ejercicio. 
Programa que  lea 100 números no nulos y luego muestre un mensaje indicando cuántos 
son positivos y cuantos negativos
'''
cont = 0
contPositivo = 0
contNegativo = 0

while cont < 100:
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