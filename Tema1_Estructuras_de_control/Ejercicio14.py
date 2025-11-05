'''
14. Ejercicio.
Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales.
'''
num1 = int(input("Dime el primer numero para saber si es el mayor: "))
num2 = int(input("Dime el segundo numero para saber si es mayor o menor: "))
if num1 > num2:
    print("El numero 1 es mayor que el numero 2")
elif num2 > num1:
    print("El numero 2 es mayor que el numero 1")
else:
    print("Los dos numeros son iguales")
