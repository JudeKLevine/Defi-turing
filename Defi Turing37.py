def nbrpre(n):
    sum = 0
    if n ==2:
        sum = 0
    elif n ==1:
        sum = 1
    else:
        for i in range(2, int(n**0.5 + 2)):
            if n%i == 0:
                sum += 1
    return sum
    
def liste(n):
    L = [int(i) for i in str(n)]
    return L
    
def retire_gauche(n):
    A = []
    a = len(str(n))
    for i in range(1,a+1):
        B = liste(n)
        C = []
        for k in range(i):
            C.append(str(B[k]))
        C = "".join(C)
        A.append(int(C))
    return A

def retire_droite(n):
    A = []
    a = len(str(n))
    for i in range(1,a+1):
        B = liste(n)
        C = []
        for k in range(i-1,a):
            C.append(str(B[k]))
        C = "".join(C)
        A.append(int(C))
    return A
        
A = [i for i in range(10,1000000) if nbrpre(i)==0]
B = []
for i in A:
    sum = 0
    for j in retire_gauche(i):
        if nbrpre(j)==0:
            sum += 1
    if sum == len(str(i)):
        B.append(i)
C = []
for i in B:
    sum = 0
    for j in retire_droite(i):
        if nbrpre(j)==0:
            sum += 1
    if sum == len(str(i)):
        C.append(i)
prinf(sum(C))
# 748317
