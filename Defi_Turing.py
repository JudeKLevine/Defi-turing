def liste(n):
    L = [int(i) for i in str(n)]
    return L
A = []
for i in range(1,250):
    for j in range(1,250):
        A.append(sum(liste(i**j)))
print(max(A))
