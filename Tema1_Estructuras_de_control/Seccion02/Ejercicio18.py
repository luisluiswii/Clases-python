'''
18. Ejercicio. 
Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia 
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla.
'''
num_base = int(input("Dime el numero que quieras elevar: "))
potencia = int (input("Hasta que numero quieres elevarlo?: "))
resultado = 0
for num_base in potencia:
    resultado = num_base * potencia
print("El resultado es: ",resultado)