'''
Dibuja un ordinograma de un programa que lea dos números y nos diga cual es mayor o si
son iguales.
'''
num1 = (int(input("Dime el primer numero para saber su orden: ")))
num2 = (int(input("Dime el segundo numero para saber su orden: ")))
if num1 == num2:
    print("EL mayor es: " + str(num1))
elif num2 > num1:
    print("El mayor es: " + str(num2))
else:
    print("los numeros son iguales")
