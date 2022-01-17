def decomp(n, a):
    A = [int(i) for i in str(n)]
    taille = len(str(a))
    L = [str(A[len(A) - taille + i]) for i in range(taille)]
    L = "".join(L)
    return int(L)

for i in range(100):
    if decomp(18**i, i) == i:
        print(i)
# 76
