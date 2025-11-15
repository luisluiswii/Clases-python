'''
17. Ejercicio. 
Programa que suma independientemente los pares y los impares de los números 
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas.
'''
contImpar= 0
contPar= 0
for i  in range(100, 200+1):
    if i % 2 == 0:
        contPar +=1
    else:
        contImpar += 1
print("Suma de pares: ", contPar, " suma de imprares: ", contImpar)