'''
35. Ejercicio. 
Realiza un programa que pida el dí-a de la semana (del 1 al 7) y escriba el día 
correspondiente. Si introducimos otro número nos da un error. 
'''
day_number = int(input("Enter the day number (1-7): "))
match day_number:
    case 1:
        day_number = "Monday"
    case 2:
        day_number = "Tuesday"
    case 3:
        day_number = "Wednesday"
    case 4:
        day_number = "Thurday"
    case 5:
        day_number = "Friday"
    case 6:
        day_number = "Saturday"
    case 7:
        day_number = "Sunday"
    case _:
        day_number = "ERROR: Incorrect number."
print(f"The day is: {day_number}")