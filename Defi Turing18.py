def div(n):
    a = 0
    for i in range(1, n//2 + 1):
        if n%i == 0: 
            a = a + i
    return a # retourne la somme des diviseurs propres d'un nombre
    
 # la liste des nombres abondants
L = [i for i in range(4000) if div(i) > i]

# la somme de deux nombres abondants
B = []
for i in L:
    for j in L:
        B.append(i+j)

A = set(B) # trier et supprimer les repetitions
result = 1007*2013 # la somme des entiers inferieurs à 2014
for i in A:
    if i ‹ 2014:result = result - i
print(result)
# 577167
