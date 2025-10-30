'''
23. Ejercicio.
Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta
que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y
cuantos negativos.
'''
positivo = 0
negativo = 0
num = -1
while num != 0:
    num = int(
        input("dime para saber el numero es negativo (para acabar escriva 0): "))
    if num == 0:
        break
    elif num < 0:
        print("Este es negativo")
        negativo += 1
    elif num > 0:
        positivo += 1
print("EXIT___Numeros positivos: " + str(positivo) +
      "___Numeros negativos: " + str(negativo))
