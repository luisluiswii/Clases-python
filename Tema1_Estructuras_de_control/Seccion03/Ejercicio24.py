'''
24. Ejercicio. 
Escribe un programa que pida un nombre de usuario y una contraseña y si se ha 
introducido "pepe" y "asdasd" se indica "Has entrado al sistema", sino se da un error.
'''
usuario = str(input("Digame su usuario: "))
contrasenya = str(input("Digame su contraseña: "))
usuario_correcto = False
contrasenya_correcta = False
if usuario != "pepe":
    print("usuario incorrecto")
else:
    print("Usuario correcto")
    usuario_correcto = True
if contrasenya != "asdasd":
    print("contraseña incorrecto")
else:
    print("contraseña correcta")
    contrasenya_correcta = True
if usuario_correcto and contrasenya_correcta:
    print("Has entrado al sistema")