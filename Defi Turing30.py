def sum5(n):
    L = [int(i) for i in str(n)]
    sum = 0
    for i in L:
        sum += i**5
    return sum
print(sum([i for i in range(1000000) if liste(i)==i])-1)
# 443839
