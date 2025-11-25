'''
33. Ejercicio. 
Realiza un programa que pida por teclado el resultado (dato entero) obtenido  al lanzar un 
dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta 
al resultado obtenido. 
Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4. 
Nota 2: Si el número del dado introducido es menor que  1 o mayor que 6, se mostrará el 
mensaje: "ERROR: número incorrecto.". 
'''
import random
oposite_face = None
dice_result = int(input("Enter the result of the dice (1-6): "))
if dice_result < 1 or dice_result > 6:
    print("ERROR: Incorrect number.")
else:
    match dice_result:
        case 1:
            oposite_face = "six"
        case 2:
            oposite_face = "five"
        case 3:
            oposite_face = "four"
        case 4:
            oposite_face = "three"
        case 5:
            oposite_face = "two"
        case 6:
            oposite_face = "one"
    print(f"The opposite face is: {oposite_face}")
    