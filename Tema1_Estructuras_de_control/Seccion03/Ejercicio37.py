'''
37. Ejercicio. 
Una compañía de transporte internacional tiene servicio en algunos países de América del 
Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se 
basa en el peso del paquete y la zona a la que va dirigido..
'''
zona = int(input("Dime la zona a la que va dirigido el paquete (América del Norte = 1, América Central = 2, América del Sur = 3, Europa = 4, Asia = 5): "))
peso = float(input("Dime el peso del paquete en kg: "))
coste_por_kg = None
if peso <= 0:
    print("El peso es incorrecto")
elif zona < 1 or zona > 5:
    print("La zona es incorrecta")
else:
    match zona:
        case 1:
            coste_por_kg = 24.00
        case 2:
            coste_por_kg = 20.00
        case 3:
            coste_por_kg = 21.00
        case 4:
            coste_por_kg = 10.00
        case 5:
            coste_por_kg = 18.00
    coste_total = coste_por_kg * peso
    print(f"El coste total del envío es: {coste_total} euros")