'''
19. Ejercicio.
Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir
'''
saldo = 1000
reirar_saldo = 0
anyadir_saldo = 0
while True:
    print("Tu saldo actual en la cuenta es: ", saldo)
    selector = int(
        input("Dime si quieres retirar diero (1) o añadir dienero a tu cuenta (2)"))
    match selector:
        case 1:
            reirar_saldo = float(
                input("Dime el saldo que deaseas retirar de la cuenta: "))
            if reirar_saldo <= 0:
                print("no debes introducir una cantidad negativa")
                break
            if saldo <= 0:
                print("Dado que su saldo es menor que 0 no puede sacar credito")
            elif (reirar_saldo >= saldo):
                saldo = saldo - reirar_saldo
        case 2:

            anyadir_saldo = float(
                input("Dime la cantidad de saldo que deseas añadir a la cuenta"))
            if anyadir_saldo <= 0:
                print("no debes introducir una cantidad negativa")
                break
            saldo = saldo + anyadir_saldo
        case _:
            print("NO SELECCIONES UNA OPCION INVALIDA")
