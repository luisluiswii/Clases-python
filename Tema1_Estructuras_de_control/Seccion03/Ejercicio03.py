'''
3.  Ejercicio. 
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. 
'''
import math
cateto1 = int(input("Dime el cateto numero 1 para calcular la hipotenusa: "))
cateto2 = int(input("Dime el cateto numero 2: "))
hipotenusa = math.sqrt((cateto1**2)+(cateto2**2))
print("Tu hipotenusa es = ", hipotenusa )