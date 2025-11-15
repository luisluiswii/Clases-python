'''
10. Ejercicio. 
Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales. 
'''
numAnteriorSuma = 1
numAnteriorProducto = 1
for i in range(1,10+1):
    numAnteriorSuma = numAnteriorSuma + i
    numAnteriorProducto = numAnteriorProducto * i
print("Suma es : ", numAnteriorSuma, "\nProducto es: " , numAnteriorProducto)    