''' 
29. Ejercicio.
Dibuja un ordinograma de un programa donde el usuario “piensa” un número del 1 al 100
y el ordenador intenta adivinarlo. Es decir, el ordenador irá proponiendo números una y otra
vez hasta adivinarlo (El usuario deberá indicarlo al ordenador si es mayor o menor o igual al
número pensado).
'''
minimo = 1
maximo = 100
respuesta = ""

print("Piensa un número del 1 al 100. El ordenador intentará adivinarlo.")

while respuesta != "=":
    num_ordenador = (minimo + maximo) // 2
    print("El número propuesto por el ordenador es:", num_ordenador)
    respuesta = input("¿Tu número es mayor (>), menor (<) o igual (=)?: ")

    if respuesta == ">":
        minimo = num_ordenador + 1
    elif respuesta == "<":
        maximo = num_ordenador - 1

print("¡El ordenador ha adivinado tu número:", num_ordenador, "!")
