def premier(n):
    sum=0
    if n==1:
        return 2
    for i in range(1, int(n**0.5+1)):
        if n%i==0:
            sum+=1
    return sum
B = [i for i in range(1200,4000) if i%2==1]
A = []
for i in range(4000,6000):
    for j in range(100):
        for k in range(6000):
            if i%2==1 and i==2*(j**2)+k and premier(k)==1:
                A.append(i)       
C = [i for i in set(A)]
for i in C:
    if i in B:
        C.remove(i)
print(C[0])
# 5777
