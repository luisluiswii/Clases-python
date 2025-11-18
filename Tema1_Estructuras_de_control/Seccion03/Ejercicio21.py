'''
21. Ejercicio. 
Algoritmo que pida un número y diga si es positivo, negativo o 0.
'''
num = int(input("Dime un numero para decirte si es positivo o negativo: "))
if num > 0:
    print("El numero es positivo ")
elif num == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")