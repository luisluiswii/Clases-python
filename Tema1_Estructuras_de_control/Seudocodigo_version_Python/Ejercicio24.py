'''
24. Ejercicio.
Dibuja un ordinograma de un programa que calcule y escriba la suma y el producto de los
10 primeros números naturales.
'''
cont = 1
suma = 0
for i in range(1, 11):
    suma = i + i
    producto = i * i
    print(str(cont) + "º suma: " + str(i) + " + " + str(i) + " = " + str(suma))
    print(str(cont) + "º producto: " + str(i) +
          " * " + str(i) + " = " + str(producto))
    print("________________________")
    cont += 1
