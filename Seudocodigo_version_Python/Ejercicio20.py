'''
20. Ejercicio. 
Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice
su factura N! siendo el factorial:
0!=1
1!=1
2!=2*1
…
N!= N*(N-1)*(N-2)*…*1
'''
num = (int(input("Dime el numero que quieras saber su factorial: ")))
factorial = 1
for i in range(1, num + 1):
    factorial = i * factorial
print(("Tu numero factorial es: ") + str(factorial))
