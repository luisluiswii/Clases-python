'''
14. Ejercicio.
Dibuja un ordinograma que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero).
'''
num1 = int(input(
    "Digame el primer numero para hacer su suma resta producto y division este numero no puede ser 0"))
num2 = int(input("Digame el segundo numero este no puede ser 0: "))
if num1 == 0 or num2 == 0:
    print(" no puede ser ninguno de los dos numeros 0 lo siento mucho")
else:
    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2
    division = num1 / num2
    print("La suma es: " + str(suma) + " la resta es: " + str(resta) +
          " el producto es: " + str(producto) + " y la división es: " + str(division))
