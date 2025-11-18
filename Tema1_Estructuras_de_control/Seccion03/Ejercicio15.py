'''
15. Ejercicio. 
Dadas  dos  variables  numéricas  A  y  B,  que  el  usuario  debe  teclear,  se  pide  realizar  un 
algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos 
variables. 
'''
a = int(input("Dime el valor a para ser intercanbiado: "))
b = int(input("Dime el valor b para ser intercanbiado: "))
a, b = b, a
print(f"Ahora la variable a vale {a} y la variable b vale {b}")
