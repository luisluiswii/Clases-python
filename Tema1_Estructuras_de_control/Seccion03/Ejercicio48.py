'''
48. Ejercicio. 
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de 
cada  mes  deposita  cantidades  variables  de  dinero;  además,  se  quiere  saber  cuánto  lleva 
ahorrado cada mes.
'''
total_hahorrado = 0
for mes in range(1, 13):
    cantidad = float(input(f"Introduce la cantidad ahorrada en el mes {mes}: "))
    total_hahorrado += cantidad
    print(f"Total ahorrado hasta el mes {mes}: {total_hahorrado} euros")
print(f"Total ahorrado en el año: {total_hahorrado} euros")
