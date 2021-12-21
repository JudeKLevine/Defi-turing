def image(n):
    A = [int(i) for i in str(n)]
    produit = 1
    for i in A:
        produit = produit*i
    return produit
def teste(n):
    while n>10:
        n = image(n)
    return n
A = [i for i in range(10,10000000) if teste(i)==6]
print(lenA)
# 318456
