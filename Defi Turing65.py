def dec_Prod(n):
    L = [int(i) for i in str(n)]
    produit = 1
    for i in L:
        produit = produit*i
    return produit
Sum = 0
for i in range(2014):
    if i + dec_Prod(i) == 2014:
        Sum = Sum + i
print(Sum)
# 7407
