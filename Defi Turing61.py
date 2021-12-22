def isole(n):
    count = 0
    L = [int(i) for i in str(n)]
    for i in range(len(L) - 2):
        if L[i] != L[i+1] and L[i+1] != L[i+2]:
            count = count + 1
    return count
for i in range(2000000, 3000000):
    if isole(i*i) == 0 and int(str(i*i)[0]) == int(str(i*i)[1]) and int(str(i*i)[-1]) == int(str(i*i)[-2]) and i%10 != 0:
        print(i)
# 2973962
