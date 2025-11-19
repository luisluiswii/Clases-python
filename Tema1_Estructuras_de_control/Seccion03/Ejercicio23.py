'''
23. Ejercicio. 
Crea un programa que pida al usuario dos números y muestre su división si el segundo no 
es cero, o un mensaje de aviso en caso contrario.
'''
num1 = int(input("Dime el primer numero para ser dividido: "))
num2 = int(input("Dime el segundo nomero para la division (no puede ser 0)"))
if num2 == 0:
    print("Error de la division el sgundo numero tiene valor 0")
else:
    resultado = num1 / num2
    print(resultado)