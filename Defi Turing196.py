def est(n):
    sum = 0
    A, B = [1,3,5,7,9], [int(i) for i in str(n)]
    for i in A:
        if i in B:
            sum += 1
    return sum
somme = 0
for i in range(13579, 97532):
    if est(i)==5:
        somme += i
print(somme)
# 6666600
