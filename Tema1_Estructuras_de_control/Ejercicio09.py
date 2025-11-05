'''
9. Ejercicio.
Dibuja un ordinograma de un programa que pida la edad por teclado y nos muestra el
mensaje de “Eres mayor de edad” o el mensaje de “Eres menor de edad”.
'''
edad = int(input("Dime tu edad para saber si eres mayor de edad"))
if (edad >= 18):
    print("Felicidades eres mayor de edad toma una cerveza")
else:
    print("Lo siento no eres mayor de edad tomate un zumito")
