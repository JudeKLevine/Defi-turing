def liste(n):
    L = [int(i) for i in str(n)]
    return L
A = []
for i in range(1000,10000):
    for j in range(100,1000):
        A.append(i*j)
B = []
for i in A:
    if liste(i) == liste(i)[::-1]:
        B.append(i)
print(max(B))
# 9744479
