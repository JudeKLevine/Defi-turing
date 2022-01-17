def decompe(n):
    L  = [int(i) for i in str(n)]
    return L

def test(List1, List2):
    count = 0
    for i in List2:
        if i in List1:
            count = count + 1
    for j in List1:
        if j in List2:
            count = count + 1
    return count

L = []
for i in range(200000):
    if test(decompe(i), decompe(i*i*i)) == len(decompe(i)) + len(decompe(i*i*i)) and i%10 != 0:
        L.append(i)
print(L[1])
# 107624
