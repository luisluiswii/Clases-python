'''
36. Ejercicio. 
Escribe un programa que pida un número entero entre uno y doce e imprima el número de 
días que tiene el mes correspondiente. Si introducimos otro número nos da un error. 
'''
days = None
month_number = int(input("Enter a month number (1-12):"))
match month_number:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        days = 31
    case 4 | 6 | 9 | 11:
        days = 30
    case 2:
        days = 28
    case _:
        days = "ERROR: Incorrect number."
print(f"The number of days is: {days}")