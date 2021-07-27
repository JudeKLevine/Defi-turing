def Liste(entier):
    List = [int(i) for i in str(entier)]
    return List
    
A = []
for i in range(1000,10000):
    for j in range(100,1000):
        A.append(i * j)
B = []
for i in A:
    if Liste(i) == Liste(i)[::-1]:
        B.append(i)
        
print(max(B))
