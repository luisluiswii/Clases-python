'''
25. Ejercicio.
Dibuja un ordinograma que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado.
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente.

'''
clasificacion = float(input(
    "Dime el resultado de tu examen para saber su resultado(el numero debe estar comprendido entre 0 y 10):"))
if clasificacion >= 0 and clasificacion <= 10:
    if clasificacion <= 3:
        print("Su nota es: Muy deficiente")
    elif clasificacion <= 5:
        print("Su nota es: Insuficiente")
    elif clasificacion <= 6:
        print("Su nota es: Suficiente")
    elif clasificacion <= 7:
        print("Su nota es: Un Bien")
    elif clasificacion <= 9:
        print("Su nota es: Notable")
    elif clasificacion <= 10:
        print("Su nota es: Sobresaliente!!!")
