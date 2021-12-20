def produit(n):
    A = [int(i) for i in str(n)]
    produit = 1
    for i in A:
        produit = produit*i
    return produit
A = []
for i in range(1000000):
    sum = 0
    while i > 10:
        i = produit(i)
        sum += 1
    A.append(sum)
print(A.index(max(A)))
# 68889
