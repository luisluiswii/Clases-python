'''
31. Ejercicio. 
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta. 

El  director  de  una  escuela  está  organizando  un  viaje  de  estudios,  y  requiere  determinar 
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. 
La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 
euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 
30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.  
Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que 
debe pagar cada alumno por el viaje. 
'''
euro = None
euros_per_student = None
students = None
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
if year < 0:
    print("The year is incorrect")
elif month < 1 or month > 12:
    print("The month is incorrect")
else:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    if day < 1 or day > max_day:
        print("The day is incorrect")
    else:
        print("The date is correct")
        students = int(input("Enter the number of students: "))
        if students >= 100:
            euros_per_student = 65
        elif students < 100 and students >= 50:
            euros_per_student = 70
        elif students >=49 and students >= 30:
            euros_per_student = 95
        elif students< 30:
            total_cost = 4000

        if students >= 30:
            total_cost = euros_per_student * students
            euro = total_cost /students
            print(f"The total const is {total_cost}€ and each student has to pay {euro}")    
        else:
            total_cost = 4000
            euros = total_cost / students
            print(f"The total const is {total_cost}€ and each student has to pay {euro}")    

        '''     
        euro = total_cost / students
        print(f"The total cost is {total_cost} euros and each student has to pay {euro} euros")
        euro = total_cost / students
        print(f"The total cost is {total_cost} euros and each student has to pay {euro} euros")
        ''' 

    
