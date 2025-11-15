'''
6.  Ejercicio. 
Programa  que  lea  un  número  positivo  N  y  calcule  y  visualice  su  factorial  N!  Siendo  el 
factorial: 
0! = 1 
1! = 1 
2! = 2 * 1 
3! = 3 * 2* 1 
N! = N * (N-1) * (N-2) * ... * .
'''
while True:
    num = int(input("Dime el numero que quieras para saber su factorial (para finalizar escriva -1): "))
    if num == -1:
        print("programa finalizado")
    if num < 0:
        print("este numero no es positivo debes introducir un numero positivo")
        continue
    factorial = 1
    for i in range(1, num+1):
        factorial *= i 
        print(factorial)