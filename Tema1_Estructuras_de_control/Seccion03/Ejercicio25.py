'''
25. Ejercicio. 
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
'''
aux = str(input("Dime una palabra para saber si empiza por mayuscula: "))
if aux.startswith(aux.upper()):
    print("Enpuza con mayuscula")
else:
    print("no empiza con mayuscula")