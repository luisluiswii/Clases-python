'''
27. Ejercicio. 
Algoritmo que pida dos números 'nota' y 'edad' y un carácter 'sexo' y muestre el mensaje 
'ACEPTADA' si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es 
'F'. En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. Si no se 
cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.
'''
nombre = str(input("Dime tu nombre: "))
sexo = str(input("Dime tu sexo (m/f)"))
nota = int(input("Dime tu nota: "))
edad = int(input("Dime tu edad: "))
mayor_edad = False
if edad >= 18:  mayor_edad = True
if mayor_edad == False:
    print(f"Lo sentimos {nombre} no cumples ta edad NO ACEPTADA")
elif sexo == 'f':
    if nota >= 5: print(f"Enorabuena {nombre} estas ACEPTADA") 
    else:print(f"Lo sentimos {nombre} no cumples ta nota NO ACEPTADA")
elif sexo == 'm':
    if nota >= 5: print(f"Enorabuena {nombre} es POSIBLE") 
    else:print(f"Lo sentimos {nombre} no cumples ta nota NO ACEPTADP")
else: print("No introdujiste un sexo correcto")