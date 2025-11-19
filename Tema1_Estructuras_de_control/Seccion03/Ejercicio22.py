'''
22. Ejercicio. 
Escribe un programa que lea un número e indique si es par o impar. 
'''
num =int(input("Dime un numero para saber si es par o inpar: "))
resultado = "par" if num % 2 == 0 else "impar"
print(f"El número {num} es {resultado}")