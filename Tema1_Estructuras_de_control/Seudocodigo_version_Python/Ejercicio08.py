'''
8. Ejercicio.
Dibuja un ordinograma de un programa que pide la edad por teclado y nos muestra el
mensaje de “Eres mayor de edad”, si y solamente si lo somos.
'''
edad = int(input("Dime tu edad para saber si eres mayor de edad: "))
if edad >= 18:
    print("Efectivamente eres mayor a 18 años")
else:
    print("No eres mayor de 18 años ")
