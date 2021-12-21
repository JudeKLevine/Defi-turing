def nbrpre(n):
    sum = 0
    for i in range(1, int(n**0.5 + 2)):
        if n%i == 0:
            sum += 1
    return sum
    
def liste(n):
    L = [int(i) for i in str(n)]
    return L
    
def perm_circ(n):
    A = []
    a = len(str(n))
    for i in range(a):
        B = liste(n)
        C = []
        for k in range(i,a):
            C.append(str(B[k]))
        for j in range(i):
            C.append(str(B[j]))
        C = "".join(C)
        A.append(int(C))
    return A
        
A = [i for i in range(100000) if nbrpre(i)==1]
B = []
for i in A:
    sum =0
    for j in perm_circ(i):
        if nbrpre(j)==1:
            sum += 1
    if sum == len(str(i)):
        B.append(i) 
print(len(B))
# 43
