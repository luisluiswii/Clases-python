'''
26. Ejercicio.
En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis, mostrar el mensaje “Excelente”
Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
Si un dado se obtiene seis, mostrar el mensaje “Regular”
Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch).
'''
import random

cont = 0
for i in range(1, 4):
    dado = random.randint(1, 6)
    print("Dado numero: ", cont, "fue: ", dado)
    if dado == 6:
        cont += 1
match cont:
    case 0:
        print("Pésimo")
    case 1:
        print("Regular")
    case 2:
        print("Muy bien")
    case 3:
        print("Excelente")
