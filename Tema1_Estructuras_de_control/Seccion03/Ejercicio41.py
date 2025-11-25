'''
41. Ejercicio. 
Realizar  un  algoritmo  que  pida  números  (se  pedirá  por  teclado  la  cantidad  de  números  a 
introducir). El  programa  debe  informar  de  cuantos  números  introducidos son mayores  que 0, 
menores que 0 e iguales a 0. 
'''
cont = int(input("Dime cuantos numeros queires introducir"))
aux = 0
cont_negativo = 0
cont_positivo = 0
cont_cero = 0
for i in range (1, cont+1):
    aux = int(input(f"Dime el {i}º  numero: "))
    if aux > 0:
        cont_positivo +=1
    elif aux == 0:
        cont_cero +=1
    else:
        cont_negativo +=1
print(f"Positivos son {cont_positivo} los negativos son {cont_negativo} y tienes {cont_cero} ceros")