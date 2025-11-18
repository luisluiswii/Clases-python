'''
19. Ejercicio. 
Escribir  un  algoritmo  para  calcular  la  nota  final  de  un  estudiante,  considerando  que:  por 
cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime 
el resultado obtenido por el estudiante. 
'''
rc = 0
ri = 0
rb = 0
preguntas_examen = int(input("Dime cuantas preguntas de examen hubo: "))
for i in range(1, preguntas_examen+1):
    selector = int(input(f"Si la pregunta {i} estubo bien dime 1 si estubo mal dime 2 y si esta en blanco dime 3: "))
    if selector == 1:
        rc +=1
    elif selector == 2:
        ri +=1
    elif selector ==3:
        rb +=1
puntos = (rc*5)-ri
print(f"en este examen saco un total de: {puntos} puntos")

