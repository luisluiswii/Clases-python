'''
6. Ejercicio.
Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
el porcentaje de descuento realizado.
'''
precio_articulo = float(input("Dime el precio del articulo: "))
precio_real = float(input("Dime el precio real: "))
descuento = (((precio_articulo - precio_real) / precio_articulo) * 100)
print("El descuento sera de: ", descuento, "%")
