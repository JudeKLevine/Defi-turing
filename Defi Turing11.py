def Mirroir(entier):
    List = [i for i in str(entier)][::-1]
    return int("".join(List))
    
A = [i for i in range(10000000) if Mirroir(i) == 4 * i]
print(max(A))
# 2199978
