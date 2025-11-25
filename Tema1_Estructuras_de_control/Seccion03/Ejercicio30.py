'''
30. Ejercicio. 
Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un 
número  divisible  por  4,  pero  no  si es  divisible  por 100, excepto  que  también  sea  divisible  por 
400.
'''
year = int(input("Tel me the year you want to know if it's a leap year:"))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("It's a leap year")    
else:
    print("It'not a leap year")    