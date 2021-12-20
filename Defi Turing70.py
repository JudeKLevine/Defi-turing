def liste(n):
    L = [int(i) for i in str(n)]
    M = [str(L[-1])]
    for i in range(len(L)-1):
        M.append(str(L[i]))
    M = "".join(M)
    return int(M) 
A = []
for i in range(100000,10000000):
    if liste(i)%i==0:
        A.append(i)
for i in A:
    if liste(i)==i:
        A.remove(i)
print(sum(A))
# 1142856
