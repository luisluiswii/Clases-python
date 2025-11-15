
altura = 5
    
for i in range(1, altura + 1):
    
    for j in range(altura - i):
        print(" ", end="")
    for k in range((2 * i) - 1):
        print("*", end="") 
    

    print()
