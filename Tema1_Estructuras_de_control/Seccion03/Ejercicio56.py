'''
56. Ejercicio. 
Mostrar  en  pantalla  los  N  primero  números  primos.  Se  pide  por  teclado  la  cantidad  de 
números primos que queremos mostrar. 
'''
N = int(input("Ingrese la cantidad de números primos que desea mostrar: "))
count = 0
num = 2
while count < N:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1
