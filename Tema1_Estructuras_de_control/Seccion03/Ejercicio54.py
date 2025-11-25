'''
54. Ejercicio. 
Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
'''
import time
segundos_totales = int(input("Dime el numero de segundos a contar: "))
horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60
print(f"Cronometro: {horas:02}:{minutos:02}:{segundos:02}")
while segundos_totales > 0:
    time.sleep(1)
    segundos_totales -= 1
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60
    print(f"Cronometro: {horas:02}:{minutos:02}:{segundos:02}")
print("¡Tiempo terminado!")
