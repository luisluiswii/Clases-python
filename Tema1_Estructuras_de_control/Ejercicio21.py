'''
21. Ejercicio.
Escriba un programa que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto.
'''
nombre_Trabajador = str(input("Dime tu nombre: "))
salario_Bruto_hora = int(
    input("Dime el salario bruto por hora del trabajador: "))
horas_trabajadas = int(input("Dime las horas trabajadas en la semana: "))

if horas_trabajadas > 35:
    salario_Bruto = (35 * salario_Bruto_hora) + \
        ((horas_trabajadas - 35) * salario_Bruto_hora * 1.5)
else:
    salario_Bruto = horas_trabajadas * salario_Bruto_hora


if salario_Bruto <= 500:
    tasas = 0
    salario_Neto = salario_Bruto
elif salario_Bruto <= 900:
    tasas = (salario_Bruto - 500) * 0.25
else:
    tasas = (400 * 0.45) + ((salario_Bruto - 900) * 0.45)

print("\nNombre del trabajador: ", nombre_Trabajador)
print("Salario bruto: ", salario_Bruto, "€")
print("Impuestos aplicados: ", tasas, "€")
print("Salario neto: ", salario_Neto, "€")
