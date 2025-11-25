'''
50. Ejercicio. 
Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km 
150, los coches tienen sentido opuesto y tienen la misma velocidad. Realizar un programa para 
determinar en qué kilómetro de esa carretera se encontrarán.
'''
km_persona1 = 70
km_persona2 = 150
while km_persona1 < km_persona2:
    km_persona1 += 1
    km_persona2 -= 1 
print(f"Los dos se encontrarán en el kilómetro {km_persona1}")
