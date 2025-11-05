'''
15. Ejercicio.
Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales
son iguales.
'''
num1 = (int(input("Dime el primer numero para saber su orden: ")))
num2 = (int(input("Dime el primer segundo para saber su orden: ")))
num3 = (int(input("Dime el primer tercer para saber su orden: ")))

if num1 == num2 == num3:
    print("Los tres números son iguales")
elif num1 == num2:
    if num1 > num3:
        print("num1 == num2 > num3")
    else:
        print("num3 > num1 == num2")
elif num1 == num3:
    if num1 > num2:
        print("num1 == num3 > num2")
    else:
        print("num2 > num1 == num3")
elif num2 == num3:
    if num2 > num1:
        print("num2 == num3 > num1")
    else:
        print("num1 > num2 == num3")

elif num1 > num2 and num1 > num3:
    if num2 > num3:
        print("num1 > num2 > num3")
    else:
        print("num1 > num3 > num2")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print("num2 > num1 > num3")
    else:
        print("num2 > num3 > num1")
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print("num3 > num1 > num2")
    else:
        print("num3 > num2 > num1")
