def Sc(n):
    Sum = 0
    L = [int(i) for i in str(n**3)]
    for i in range(len(L)):
        Sum = Sum + L[i]
    return Sum
L = [i for i in range(1000) if Sc(i) == i]
print(L[-1])
# 27
