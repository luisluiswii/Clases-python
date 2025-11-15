'''
15. Ejercicio. 
Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos 
la altura de la pirámide por teclado. Este es un ejemplo:
'''
altura = int(input("Introduce la altura de la escalera: "))
for i in range(altura, 0, -1):
    print(" " * (altura - i) +  "* " *i)