'''
7.  Ejercicio. 
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas 
horas y minutos corresponde.clear()
'''
hh=0
leer_min = int(input("Dime cuantos minutos quieres pasar: "))
while leer_min>= 60:
    hh +=1
    leer_min -= 60
print("Tenemos: ",hh,"h ",leer_min,"min")