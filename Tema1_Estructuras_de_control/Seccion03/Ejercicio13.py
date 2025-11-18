'''
13. Ejercicio. 
Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
Python3  no  tiene  ninguna  función  predefinida  que  permita  calcular  la  raíz  cúbica,  ¿Cómo  se 
puede calcular? 
'''
import math
num = float(input("Dime el numero que quieras operar: "))
raizCuadrada = math.sqrt(num)
raizCubica = math.copysign(abs(num) ** (1/3), num)
print(f"El resultado de la raiz cuadrada es {raizCuadrada} y la cubica {raizCubica}")