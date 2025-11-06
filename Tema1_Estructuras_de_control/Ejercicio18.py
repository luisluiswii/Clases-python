'''
18. Ejercicio.
Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de 10.
'''
num = int(input("Dime el numero para saber si es nuemero de 10: "))
if (num % 10 == 0):
    print("El numero es multiplo de 10")
else:
    print("El numero no es multiplo de 10")
