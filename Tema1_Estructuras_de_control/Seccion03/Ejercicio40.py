'''
40. Ejercicio. 
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la 
media de todos los números introducidos.
'''
sum_numbers = 0
count_numbers = 0
while True:
    user_input = int(input("Enter a number (0 to stop): "))
    if user_input == 0:
        break
    sum_numbers += user_input
    count_numbers += 1
if count_numbers > 0:
    average = sum_numbers / count_numbers
    print(f"The sum of the numbers is: {sum_numbers}")
    print(f"The average of the numbers is: {average}")
else:
    print("No numbers were entered.")
