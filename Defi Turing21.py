def teste(n):
    sum = 0
    A = [int(i) for i in str(n)]
    for i in A:
        if A.count(i)==1:
            sum+=1
    return sum
A = [i for i in range(1, 2014) if teste(i)==len(str(i))]
max = 0
for i in range(1242):
    a = A[i+1]-A[i]
    if a > max:
        max = a
print(max*len(A))
# 130515
