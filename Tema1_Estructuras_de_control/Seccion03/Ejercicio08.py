'''
8.  Ejercicio. 
Un  vendedor  recibe  un  sueldo  base  más  un  10%  extra  por  comisión  de  sus  ventas,  el 
vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas 
que  realiza  en  el  mes  y  el  total  que  recibirá  en  el  mes  tomando  en  cuenta  su  sueldo  base  y 
comisiones.
'''

comisiones = 0
sueldoTotal = 0

for i in range(1, 4):
    sueldoBase = float(input(f"{i}º Venta  - Dime el monto de la venta: "))
    bono = sueldoBase * 0.10
    print("Tu comisión por esta venta fue: ", bono)
    comisiones += bono
    sueldoTotal += sueldoBase

totalGanado = sueldoTotal + comisiones
print("\nResumen del mes:")
print("Sueldo base total: ", sueldoTotal)
print("Comisiones totales: ", comisiones)
print("Total ganado en el mes: ", totalGanado)
