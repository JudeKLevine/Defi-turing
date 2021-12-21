def liste(n):
    L = [int(i) for i in str(n)]
    return L
def tst(L):
    A = []
    for i in L:
        if L.count(i)==1:
            A.append(1)
        else:
            A.append(0)
    if 0 in A:
        a = 0
    else :
        a = 1
    return a
A = [i for i in range(100000) if tst(liste(i))==1]
print(sum(A))
# 1520464455
