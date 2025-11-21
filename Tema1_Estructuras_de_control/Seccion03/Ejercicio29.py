'''
29. Ejercicio. 
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los 
lados  de  un  triángulo.  El  programa  debe  determinar  qué  tipo  de  triángulo  es,  teniendo  en 
cuenta: 
• Si se cumple Pitágoras entonces es triángulo rectángulo 
• Si sólo dos lados del triángulo son iguales entonces es isósceles. 
• Si los 3 lados son iguales entonces es equilátero. 
• Si no se cumple ninguna de las condiciones anteriores, es escaleno.
'''
lado_a = float("Dime las medidas de lado a del triangulo para saber que tipo de triangulo es: ")
lado_b = float("Dime el lado b: ")
lado_c = float("Dime el lado c: ")
if lado_a == lado_b == lado_c:
    print("El triangulo es equilatero")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("El triangulo es isosceles")
elif (lado_a**2 + lado_b**2 == lado_c**2) or (lado_a**2 + lado_c**2 == lado_b**2) or (lado_b**2 + lado_c**2 == lado_a**2):
    print("El triangulo es rectangulo")
else:
    print("El triangulo es escaleno")
