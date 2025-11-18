'''
9.  Ejercicio. 
Una  tienda  ofrece  un  descuento  del  15%  sobre  el  total  de  la  compra  y  un  cliente  desea 
saber cuánto deberá pagar finalmente por su compra. 
'''
montoTotal = float(input("Dime cuanto es el total de la compra: "))
descuento = montoTotal * 0.15
montoFinal = montoTotal - descuento
print("El descuento aplicado fue: ", descuento)
print("El monto final a pagar es: ", montoFinal)