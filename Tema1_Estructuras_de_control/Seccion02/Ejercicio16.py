'''
16. Ejercicio. 
Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con 
el valor -1 y nos dice si hubo o no alguna nota con valor 10.
'''
aprobado = False
contDices = 0
while True:
    select = int(input("Dime la nota que sacaste entre 1 y 10. (-1 para terminar): "))
    match (select):
        case 0:
            print("Suspenso")
        case 1:
            print("Suspenso")
        case 2:
            print("Suspenso")
        case 3:
            print("Suspenso")
        case 4:
            print("Suspenso")
        case 5:
            print("Aprobado")
        case 6:
            print("Aprobado")
        case 7:
            print("Aprobado")
        case 8:
            print("Aprobado")
        case 9:
            print("Aprobado")
        case 10:
            print("Aprobado")
            aprobado = True
            contDices += 1
        case -1:
            print("Finalizando programa....")
            break
        case _:
            print("Numero equivocado")
            continue
if aprobado != True:
    print("No hubo ningun 10")
else:
    print("Hubo: ", contDices, " dieces")