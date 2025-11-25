'''
44. Ejercicio. 
Realizar  un  algoritmo  que  muestre  la  tabla  de  multiplicar  de  un  número  introducido  por 
teclado.
'''
resultado = 0
num = int(input("Dime el numero que quieras saber su tabla de multiplicar: "))
for i in range(1, 11):
 print(f"{num} x {i} = {num * i}")