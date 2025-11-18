'''
12. Ejercicio. 
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. 
Calcula y muestra la distancia entre ellos.
        y
        ^
     3  |          
     2  |          
     1  |       (x2,y2)
--------+-------> x
    -1  |          
    -2  |   (x1,y1)
    -3  |          

'''
import math
x1 = float(input("Dime la ubicación de la x1 que quieras: "))
y1 = float(input("Dime la ubicación de la y1 que quieras "))
x2 = float(input("Dime la ubicación de la x2 que quieras: "))
y2 = float(input("Dime la ubicación de la y2 que quieras "))
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distancia entre los dos sera de {distancia}")
