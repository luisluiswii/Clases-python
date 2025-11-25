'''
46. Ejercicio. 
Escribe un programa que dados dos números, uno real (base)  y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de 
potencia.
'''
base = float(input("Dime la base (numero real): "))
exponente = int(input("Dime el exponente (entero positivo): "))
resultado = 1.0
for i in range(exponente):
    resultado *= base
print(f"El resultado de {base} elevado a la {exponente} es: {resultado}")
