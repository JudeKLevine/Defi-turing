A = [i for i in range(1,9)]
L = []
for i in range(600):
    L.append([7*i + j for j in A])
B = []
for i in L:
    if L.index(i)%2==0:
        B.append(i)
    else:
        B.append(i[::-1])



D = [i for i in range(1,8)]
M = []
for i in range(600):
    M.append([6*i + j for j in D])

E = []
for i in M:
    if M.index(i)%2==0:
        E.append(i)
    else:
        E.append(i[::-1])
        
sum = []

for i in range(len(E)):
    for j in range(len(E)):
        if E[i][1]==B[j][1] and B[i][1]:
            sum.append(E[i][1])
a = 0
for i in sum:
    if i < 2013:
        a+=i
print(a)
# 94848
