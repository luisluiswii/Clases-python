'''
5.  Ejercicio. 
Programa que muestre en líneas separadas lo siguiente: 
ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA, 
WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A.
'''
texto = "ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA, WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A."
texto = texto.replace(",", "\n")
print (texto)