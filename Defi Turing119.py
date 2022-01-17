def decompe(n): # decomposition en produit de facteur premier
    a = 2
    b = n
    List = []
    for i in range(2, n//2+1):
        if n%i == 0:
            while n%i == 0:
                List.append(i)
                n=n//i
    if n == b : List.append(b)
    return List 

L = []
for i in range(2, 51):
    L = L + decompe(i)
    
Copy = L
L = set(L)

produit = 1
for i in L: produit = produit * (Copy.count(i) + 1)
print(produit)
# 4464046080
