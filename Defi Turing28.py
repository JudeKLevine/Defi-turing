def spirale(n): # il faut que n soit impair$
    colonne = []
    for i in range((n-1)//2):
        colonne.append((2*((n-1)//2 - i) + 1)**2 - ((n-1)//2 - i)) 
    for i in range((n-1)//2 + 1):
        colonne.append((2*i - 1)**2 + 3*i)
    return 2*sum(colonne) - 1

print(spirale(2013))
# 5440039565
