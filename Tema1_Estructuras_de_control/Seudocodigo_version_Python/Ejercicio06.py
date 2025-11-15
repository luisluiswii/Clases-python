'''
6. Ejercicio.
Dibuja un ordinograma que dado el precio de un artículo y el precio de venta real nos
muestre el porcentaje de descuento realizado
'''
precioArticulo = float(input("dime el precio del articulo: "))
precioReal = float(input("dime el precio real del articulo: "))
resultado = (((precioArticulo - precioReal) / precioArticulo) * 100)
print("el porcenmtaje de descuento es de: " + str(resultado) + "%")
