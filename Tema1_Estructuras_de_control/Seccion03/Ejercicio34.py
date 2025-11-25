'''
34. Ejercicio. 
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
'''
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