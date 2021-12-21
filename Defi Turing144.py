def liste(n):
    L = [int(i) for i in str(n)]
    return L
A = [i for i in range(100000,1000000) if liste(i).count(7)==1]
C = []
for i in A:
    if max(liste(i)) ‹ 8:
        C.append(i)
print(len(C))
# 88837
