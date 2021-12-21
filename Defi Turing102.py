def somme(n):
    A = [int(i) for i in str(n)]
    sum = 0
    for i in A:
        sum += i**7
    return sum
A = [i for i in range(1000000,10000000) if somme(i)==i]
print(sum(A))
# 25679675
