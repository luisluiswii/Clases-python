'''
25. Ejercicio.
La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch).
'''
mensualidad = 0
matricula = 0
nombre = (input("Dime el nombre del postulante: "))
facultad = (input("Dime la facultad que va a cursar(Ing.Sistemas/Derecho/Ing.Naviera/Ing.Pesquera/Contabilidad/Administracion): ").strip().lower())

match facultad:
    case "ing.sistemas":
        matricula = 350
        mensualidad = 650
        print("Tu matricula es e 350 y tu mensualidad de 650")
    case "derecho":
        matricula = 300
        mensualidad = 550
        print("Tu matricula es e 300 y tu mensualidad de 550")
    case "ing.naviera":
        matricula = 300
        mensualidad = 500
        print("Tu matricula es e 300 y tu mensualidad de 500")
    case "ing.pesquera":
        matricula = 310
        mensualidad = 460
        print("Tu matricula es e 310 y tu mensualidad de 460")
    case "contabilidad":
        matricula = 280
        mensualidad = 490
        print("Tu matricula es e 280 y tu mensualidad de 490")
    case "administracion":
        matricula = 360
        mensualidad = 520
        print("Tu matricula es e 360 y tu mensualidad de 520")
    case _:
        print("Esta facultad no existe")

igv = (matricula + mensualidad) * 0.18
monto_final = matricula + mensualidad + igv
print(f"El nombre del postulante es: {nombre}")
print(f"El IGV es: {igv}")
print(f"El monto final a pagar es: {monto_final}")
