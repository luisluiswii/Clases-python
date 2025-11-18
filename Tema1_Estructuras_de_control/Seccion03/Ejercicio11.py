'''
11. Ejercicio. 
Pide  al  usuario  dos  números  y muestra  la  "distancia"  entre  ellos  (el  valor  absoluto  de  su 
diferencia, de modo que el resultado sea siempre positivo)
'''
num1 = float(input("Dime tu primer numero: "))
num2 = float(input("Dime tu segundo numero: "))
distancia = num1 - num2
if distancia < 0:
    distancia *= -1
print(f"La distancia entre el punto a y el punto b es de {distancia} numeros")