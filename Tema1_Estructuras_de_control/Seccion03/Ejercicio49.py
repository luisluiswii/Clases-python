'''
49. Ejercicio. 
Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la 
semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por 
las horas trabajadas.
'''
total_horas = 0
for dia in range(1, 7):
    horas = float(input(f"Dime las horas trabajadas el día {dia}: "))
    total_horas += horas
sueldo_por_hora = float(input("Dime el sueldo por hora: "))
sueldo_total = total_horas * sueldo_por_hora
print(f"El total de horas trabajadas es: {total_horas}")
print(f"El sueldo total a recibir es: {sueldo_total}")
