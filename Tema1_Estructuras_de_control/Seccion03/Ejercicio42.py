'''
42. Ejercicio. 
Algoritmo  que  pida  caracteres  e  imprima  'VOCAL'  si  son  vocales  y  'NO  VOCAL'  en  caso 
contrario, el programa termina cuando se introduce un espacio. 
'''
while True:
    aux = input("Introduce un caracter (espacio para salir): ")
    if len(aux) != 1:
        print("Hubo un error solo admitimos un caracter")
    elif aux in ['a', 'e', 'i', 'o', 'u']:
        print(f"Tu caracter {aux} = VOCAL")
    elif aux in ['b', 'c', 'd', 'f', 'g', 'h', 'j',' k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
        print(f"Tu caracter {aux} = NO VOCAL")
    elif aux == ' ':
        print("Cerrando programa..")
        break
    else:
        print("caracter erroneo")
    