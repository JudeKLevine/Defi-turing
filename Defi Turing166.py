def Sum(N):
    L = [int(i) for i in str(N)]
    return sum(L)
B = [0 for i in range(55)]
for i in range(1000000):
    B[Sum(i)] = B[Sum(i)] + 1 
print(B.index(max(B)), max(B))
# 27 55252
