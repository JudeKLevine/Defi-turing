def Fusion(int1, int2):
    List = [i for i in str(int1)]
    for i in str(int2):
        List.append(i)
    result = int("".join(List))
    return result
    
for i in range(1000, 10000):
    for j in range(1000, 10000):
        if i * i + j * j == Fusion(i, j): print(i, j)
# 94122353
