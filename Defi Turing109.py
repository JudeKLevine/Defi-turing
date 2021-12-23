def dif(n):
    L = [int(i) for i in str(n)]
    b = 0
    for i in L:
        if L.count(i) == 1: b = b + 1
    if b == len(L) : return 1
    else :           return 0
    
def DIF(L, M):
    a = 0
    l = [int(i) for i in str(L)]
    m = [int(i) for i in str(M)]
    for i in l:
        if i not in m:
            a = a + 1
    if a == len(l) : return 1
    else : return 0
    
L = []    
for i in range(1000, 10000):
    if dif(i) == 1 and dif(2*i) == 1 and (2*i)/10000 > 1 and DIF(i, 2*i) == 1:
        L.append(2*i)

print(L[0] + L[-1])  # 29180
