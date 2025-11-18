'''
18. Ejercicio. 
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales. Mostramos las 
Iniciales en Mayúsculas sí o sí.
'''
nombre = str(input("Dime tu nombre: "))
apellido1 = str (input("Dime tu primer apelldo: "))
apellido2 = (input("Dime tu segundo apellido:"))
inicial_nombre = nombre[0].upper()
inicial_apellido1 = apellido1[0].upper()
inicial_apellido2 = apellido2[0].upper()
print(f"Tus iniciales son {inicial_nombre, inicial_apellido1, inicial_apellido2 }")