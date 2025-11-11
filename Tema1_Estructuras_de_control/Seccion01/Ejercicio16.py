'''
16. Ejercicio.
Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene.
'''
num = str(input("Dime un número entre 0 y 99999: "))
if 0 <= int(num) <= 99999:
    cifras = len(num)
    print("El número tiene", cifras, "cifras")
else:
    print(" El número no está en el rango permitido")
