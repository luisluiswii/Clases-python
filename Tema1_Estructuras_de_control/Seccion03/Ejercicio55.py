'''
55. Ejercicio. 
Realizar  un  ejemplo  de  menú,  donde  podemos  escoger  las  distintas  opciones  hasta  que 
seleccionamos la opción de "Salir". 
'''
while True:
    print("Menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == '1':
        print("Has seleccionado la Opción 1.")
    elif opcion == '2':
        print("Has seleccionado la Opción 2.")
    elif opcion == '3':
        print("Has seleccionado la Opción 3.")
    elif opcion == '4':
        print("Saliendo del menú. ¡Hasta luego!")
        break
    else:
        print("Opción no válida, por favor selecciona una opción del 1 al 4.")