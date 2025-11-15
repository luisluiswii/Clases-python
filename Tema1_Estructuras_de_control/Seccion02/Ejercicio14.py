'''
14. Ejercicio. 
Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura 
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura:

'''

altura = int(input("Introduce la altura de la escalera: "))
for i in range(1, altura+1):
    print(" " * (altura - i)+ "* " * i )
    
    
for i in range(altura, 0, -1):
    print(" " * (altura - i) +  "* " *i)