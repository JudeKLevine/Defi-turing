from math import factorial

def Liste(entier):
    List = [int(i) for i in str(entier)]
    return List
    
print(sum(Liste(factorial(2013))))
# 24021
