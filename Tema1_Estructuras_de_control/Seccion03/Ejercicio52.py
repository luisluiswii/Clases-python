'''
52. Ejercicio. 
Una  empresa  les  paga  a  sus  empleados  con  base  en  las  horas  trabajadas  en  la  semana. 
Realice un algoritmo para determinar el sueldo semanal de  N trabajadores y, además, calcule 
cuánto pagó la empresa por los N empleados. 
'''
total_pagado = 0
N = int(input("Ingrese el número de trabajadores: "))
for i in range(1, N + 1):
    horas_trabajadas = float(input(f"Ingrese las horas trabajadas por el trabajador {i}: "))
    sueldo_por_hora = float(input(f"Ingrese el sueldo por hora del trabajador {i}: "))
    sueldo_semanal = horas_trabajadas * sueldo_por_hora
    print(f"El sueldo semanal del trabajador {i} es: {sueldo_semanal}")
    total_pagado += sueldo_semanal
print(f"El total pagado por la empresa a los {N} empleados es: {total_pagado}")
