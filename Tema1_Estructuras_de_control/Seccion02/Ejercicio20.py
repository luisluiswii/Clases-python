'''20. Ejercicio. 
Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de 
5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad 
(utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible. 
Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100 
€, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque 
sume 145 € no es el mínimo número de billetes posible).
'''

numero_de_billetes_de_500 = 0
numero_de_billetes_de_200 = 0
numero_de_billetes_de_100 = 0
numero_de_billetes_de_50 = 0
numero_de_billetes_de_20 = 0
numero_de_billetes_de_10 = 0
numero_de_billetes_de_5 = 0
multiplo_5 = False

while not multiplo_5:
    dinero = int(input(
        "Cuanto dienero quieres en billetes?(el numero debe ser en multiplos de 5)"))
    if dinero % 5 == 0 or dinero == 5:
        multiplo_5 = True
while dinero >= 500:
    dinero -= 500
    numero_de_billetes_de_500 += 1
while dinero >= 200:
    dinero -= 200
    numero_de_billetes_de_200 += 1
while dinero >= 100:
    dinero -= 100
    numero_de_billetes_de_100 += 1
while dinero >= 50:
    dinero -= 50
    numero_de_billetes_de_50 += 1
while dinero >= 20:
    dinero -= 20
    numero_de_billetes_de_20 += 1
while dinero >= 10:
    dinero -= 10
    numero_de_billetes_de_10 += 1
while dinero >= 5:
    dinero -= 5
    numero_de_billetes_de_5 += 1
print("\nBilletes necesarios para alcanzar la cantidad:")
if numero_de_billetes_de_500 > 0:
    print(f"{numero_de_billetes_de_500} billete(s) de 500 €")
if numero_de_billetes_de_200 > 0:
    print(f"{numero_de_billetes_de_200} billete(s) de 200 €")
if numero_de_billetes_de_100 > 0:
    print(f"{numero_de_billetes_de_100} billete(s) de 100 €")
if numero_de_billetes_de_50 > 0:
    print(f"{numero_de_billetes_de_50} billete(s) de 50 €")
if numero_de_billetes_de_20 > 0:
    print(f"{numero_de_billetes_de_20} billete(s) de 20 €")
if numero_de_billetes_de_10 > 0:
    print(f"{numero_de_billetes_de_10} billete(s) de 10 €")
if numero_de_billetes_de_5 > 0:
    print(f"{numero_de_billetes_de_5} billete(s) de 5 €")

