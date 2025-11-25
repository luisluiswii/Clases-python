'''
43. Ejercicio. 
Escribir  un  programa  que  imprima  todos  los  números  pares  entre  dos  números  que  se  le 
pidan al usuario.
'''
inicio = int(input("Dime el inicio: "))
fin = int(input("Dime el fin: "))
while True:
    if 0 == inicio % 2:
        print(f"El numero {inicio} es par")
    if inicio == fin:
        break
    inicio +=1
    