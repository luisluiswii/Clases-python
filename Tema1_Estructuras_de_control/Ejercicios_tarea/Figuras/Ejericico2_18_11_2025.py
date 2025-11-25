'''
4
4 4
4  4
4   4
444444
'''
altura = 4  

for i in range(altura):
    linea = "4"
    if i > 0:
        linea += " " * (i - 1) + "4"
    print(linea)
print("4" * (altura + 1))


