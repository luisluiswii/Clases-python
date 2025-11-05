'''
4. Ejercicio.
Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división.
'''
num1 = int(input(
    "Escriba el primer numero para calcular su summa, resta, producto y división (no puede ser 0): "))
num2 = int(input("Escriba el segundo numero (no puede ser 0): "))
if (num1 == 0 or num2 == 0):
    print("Lo siento esta calculadora no trabaja con 0")
else:
    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2
    division = num1 / num2
    print("La suma es: ", suma, "\nLa resta es: ", resta,
          "\nEl producto es: ", producto, "\nLa división es: ", division)
