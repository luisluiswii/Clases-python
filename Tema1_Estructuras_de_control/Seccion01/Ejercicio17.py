'''
17. Ejercicio.
Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto
'''
print("Simulador de inicio de sesión")

usuario = str(input("Registre su nombre de usuario: "))
contrasenya = str(input("Registre su contraseña: "))

introducir_usuario = str(input("Introduzca su nombre de usuario: "))
introducir_contrasenya = str(input("Introducir su contraseña: "))

if usuario != introducir_usuario:

    print("Hubo un error su nombre es distintas de la usada para su registro")
elif contrasenya != introducir_contrasenya:
    print("Hubo un error su contraseña es distintas de la usada para su registro")
else:
    print("Inicio de sesion exitoso!!!!")
