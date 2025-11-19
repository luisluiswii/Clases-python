'''
26. Ejercicio. 
Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el 
exponente. Pueden ocurrir tres cosas: 
• El exponente sea positivo, sólo tienes que imprimir la potencia. 
• El exponente sea 0, el resultado es 1. 
• El exponente sea negativo, el resultado es 1/potencia con el exponente positivo. 
'''
base = float(input("Dime la base que desees para calcular: "))
exponente = float(input("Dime exponente (si escrives 0 sera considerado como 1): "))
if exponente == 0:
    resultado = 1
elif exponente< 0:
    resultado = 1/(base ** abs(exponente))
else:
    resultado = 0 