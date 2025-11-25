'''
45. Ejercicio. 
Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior 
es  mayor  que  el  superior  lo  tiene  que  volver  a  pedir.  A  continuación,  se  van  introduciendo 
números  hasta  que  introduzcamos  el  0.  Cuando  termine  el  programa  dará  las  siguientes 
informaciones: 
• La suma de los números que están dentro del intervalo (intervalo abierto). 
• Cuantos números están fuera del intervalo. 
• He informa si hemos introducido algún número igual a los límites del intervalo. 
'''
inferior = int(input("Dime el limite inferior del intervalo: "))
superior = int(input("Dime el limite superior del intervalo: "))
while inferior >= superior:
    print("El limite inferior debe ser menor que el superior. Intentalo de nuevo.")
    inferior = int(input("Dime el limite inferior del intervalo: "))
    superior = int(input("Dime el limite superior del intervalo: "))
suma_dentro = 0
cont_fuera = 0
igual_limites = False
while True:
    numero = int(input("Introduce un numero (0 para terminar): "))
    if numero == 0:
        break
    if inferior < numero < superior:
        suma_dentro += numero
    elif numero < inferior or numero > superior:
        cont_fuera += 1
    if numero == inferior or numero == superior:
        igual_limites = True
print(f"La suma de los numeros dentro del intervalo es: {suma_dentro}")
print(f"Cantidad de numeros fuera del intervalo: {cont_fuera}")
if igual_limites:
    print("Se ha introducido al menos un numero igual a los limites del intervalo.")
else:
    print("No se ha introducido ningun numero igual a los limites del intervalo.")
    