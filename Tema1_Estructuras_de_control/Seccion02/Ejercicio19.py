'''
19. Ejercicio. 
Programa  donde  el  usuario  "piensa"  un  número  del  1  al  100  y  el  ordenador  intenta 
adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el 
usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado).  
'''
import random

minimo=1
maximo = 1
intentos = 0

while True:
    intentos += 1
    propuesta = random.randint(minimo, maximo)
    print("¿Es ", propuesta, " ?")
    respuesta = input("Responde (mayor/menor/igual): ").lower()

    if respuesta == "igual":
        print("¡Adivinado en ", intentos, " intentos!")
        break
    elif respuesta == "mayor":
        minimo = propuesta + 1
    elif respuesta == "menor":
        maximo = propuesta - 1
