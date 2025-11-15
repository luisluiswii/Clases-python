'''
7.  Ejercicio. 
Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún 
número negativo o no. 
'''
cont = 0

while cont < 100:
    num= int(input("Dime un numero no nulo"))
    if num == 0:
        print("numero no valido")
        continue
    if num < 0:
        print("numero negativo")
    cont += 1
    