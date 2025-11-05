'''
5. Ejercicio.
Escriba un programa que toma como dato de entrada un número que corresponde a la
longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera
que corresponde con dicho radio.
'''
import math
pi = math.pi
radio = float(input("Dime la longitud del radio"))
diametro = radio * 2
longitud_circunferencia = pi * diametro
area_circunferencia = pi * (radio ** 2)
print("El el radio es: ", radio, "\nEl  diametro es: ", diametro, "\nLa longitud de la circunferencia ",
      longitud_circunferencia, "\nEl area de la circunferencia es: ", area_circunferencia)
