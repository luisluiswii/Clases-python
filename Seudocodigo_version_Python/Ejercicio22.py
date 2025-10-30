'''
22. Ejercicio.
Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje indicando cuántos son positivos y cuantos negativos.
'''
num = 1
negativo = 0
positivo = 0
for i in range(1, 100):
    num = (input("dime para saber el numero es negativo"))
    if num <= 0:
        print("Este es negativo")
        negativo = + 1
    else:
        positivo = + 1
