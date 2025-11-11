'''
23. Ejercicio.
Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra.
'''
original_cost = float(input("Cuanto te cuesta el producto"))
selector = input("Quieres pagar con targeta o con efectivo (t/e)")

if selector == "t":
    recargo = original_cost * 0.03
    total = original_cost + recargo
    print("Recargo con targeta: ", recargo, "€")
    print("Total a pagar: ", total, "€")
elif selector == "e":
    descuento = original_cost * 0.05
    total = original_cost - descuento
    print("Descuento por pago efectivo: ", descuento, "€")
    print("Total a pagar: ", total, "€")
else:
    print("Eleccion invalida 't' para targeta y 'e' para efectivo")
