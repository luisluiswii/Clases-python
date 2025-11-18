'''
10. Ejercicio. 
Un  alumno  desea  saber  cuál  será  su  calificación  final  en  la  materia  de  Algoritmos  Dicha 
calificación se compone de los siguientes porcentajes: 
• 55% del promedio de sus tres calificaciones parciales. 
• 30% de la calificación del examen final. 
• 15% de la calificación de un trabajo final.
'''
promedio = 0
totalParciales = 0
calificacionExamen = 0
calificacionTrabajo = 0
aux = 0
for i in range(1, 4):
    aux = float(input(f"Dime la nota de tu {i}º parcial:"))
    totalParciales += aux
promedio = (totalParciales / 3) * 0.55
calificacionExamen = float(input("Dime la nota del examen final: ")) * 0.30
calificacionTrabajo = float(input("Dime la nota del trabajo final: ")) * 0.15
calificacionFinal = (totalParciales + calificacionTrabajo + calificacionTrabajo)
print("Tu calificacion final es de: ", calificacionFinal )
