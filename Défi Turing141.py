def image(int):
    A = [int(i) for i in str(int)]
    produit = 1
    for i in A:
        produit = produit * i
    return produit
    
def teste(int):
    while int > 10:
        int = image(int)
    return int
    
A = [i for i in range(10,10000000) if teste(i)==6]
print(len(A))
