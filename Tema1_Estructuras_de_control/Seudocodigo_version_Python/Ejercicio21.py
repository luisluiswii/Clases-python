'''
21. Ejercicio.
Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje de si ha leído número negativo o no.
'''
num = 1
for i in range(100):
    num = (input("dime para saber el numero es negativo"))
    if num <= 0:
        print("Este es negativo")
