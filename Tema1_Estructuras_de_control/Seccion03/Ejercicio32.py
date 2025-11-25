'''
32. Ejercicio. 
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta. 

La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro 
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los 
siguientes  tres,  80  céntimos,  los  siguientes  dos  minutos,  70  céntimos,  y  a  partir  del  décimo 
minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, 
en turno de mañana, 15 %, y en turno de tarde, 10 %.   
Realice un algoritmo para determinar cuánto debe pagar por cada concepto  una persona 
que realiza una llamada.
'''
cost = None
min_call = None
week_day = None
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
        min_call = int(input("Tell me how many minutes the call Lasted: "))
        week_day = input("Enter the day of the week you made the call (e.g., Monday, Tuesday, etc.): ")
        if min_call <= 5:
            cost = 1
        elif min_call > 5 and min_call <= 8:
            cost = 1 + (min_call - 5) * 0.8
        elif min_call > 8 and min_call <= 10:
            cost = 1 + 3 * 0.8 + (min_call - 8) * 0.7
        else:
            cost = 1 + 3 * 0.8 + 2 * 0.7 + (min_call - 10) * 0.5
        if week_day.lower() == "sunday":
            cost += cost * 0.03
        else:
            time_turn = input("Enter the time turn you made the call (morning/afternoon): ")
            if time_turn.lower() == "morning":
                cost += cost * 0.15
            else:
                cost += cost * 0.10
        print(f"The total cost of the call is: {cost} euros")
        
            