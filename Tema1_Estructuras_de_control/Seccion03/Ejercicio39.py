'''
39. Ejercicio. 
Crea  una  aplicación  que  permita  adivinar  un  número.  La  aplicación  genera  un  número 
aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si el número a 
adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 
intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en 
cuantos  intentos  lo  has  acertado),  si  se  llega  al  límite  de  intentos  te  muestra  el  número  que 
había generado.
'''
import random
number_to_guess = random.randint(1, 100)
attempts = 10
while attempts > 0:
    user_guess = int(input("Guess the number (between 1 and 100): "))
    attempts -= 1
    if user_guess < number_to_guess:
        print(f"The number to guess is higher. You have {attempts} attempts left.")
    elif user_guess > number_to_guess:
        print(f"The number to guess is lower. You have {attempts} attempts left.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
        break
if attempts == 0 and user_guess != number_to_guess:
    print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")