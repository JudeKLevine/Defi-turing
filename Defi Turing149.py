def sameInt(N,n):
    a = 0
    b = 0
    for i in str(N):
        if i in str(n): a = a + 1
    for i in str(n):
        if i in str(N): b = b + 1
    if a == len(str(N)) and b == len(str(n)): return 1
    else : return 0
a = 100000000

for i in range(1,91800):
    q = a//i
    r = a%i
    if sameInt(i, q) == 1 and sameInt(i,r) == 1: print(i)
# 31622
