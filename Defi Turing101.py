def sum3(n):
    sum = 0
    L = [int(i) for i in str(n)]
    for i in L:
        sum += i**3
    return sum
A = [i for i in range(1000000) if i%11==0]
B = [i for i in A if i/11==sum3(i)]
printf(sum(B))
# 22209
