'''
24. Ejercicio.
Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra.
'''
montoCompra = float(input("Ingrese el monto de la compra: "))
diaSemana = input("Ingrese el día de la semana: ").strip().lower()
if diaSemana == "martes" or diaSemana == "jueves":
    descuento = montoCompra * 0.15
    totalPagar = montoCompra - descuento
    print("Decuento aplicado: ", descuento, "€",
          "Total a pagar: ", totalPagar, "€")
else:
    print("El total a pagar sera ", montoCompra,
          "€ \n y no tendra descuento devido a que no es ni martes ni jueves")
