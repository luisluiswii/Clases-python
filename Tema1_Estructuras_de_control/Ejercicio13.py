'''
13. Ejercicio.
Escriba un programa que lea dos números y lo visualiza en orden ascendente.
'''
num1 = int(input("Dime el primer numero para saber si es el mayor: "))
num2 = int(input("Dime el segundo numero para saber si es mayor o menor: "))
if num1 > num2:
    print("El numero 1: ", num1, "<--- numero 2: ", num2)
elif num2 > num1:
    print("El numero 2: ", num2, "<--- numero 2: ", num1)
else:
    print("El numero 1: ", num1, "==== numero 2: ", num2)
