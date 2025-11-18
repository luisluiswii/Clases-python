'''
5.  Ejercicio. 
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
'''
gradosFahrenheit = float(input("Dime cuantos grados tienes para pasarlos a Celsius: "))
gradosCelsius = (gradosFahrenheit - 32) * 5 / 9
print("Aqui tienes tu resultado en celsius: ", gradosCelsius)