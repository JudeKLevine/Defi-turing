def binaire(n):
    L = []
    if type(n) != type(1) or n‹0:
        return None
    while n >0:
        L.append(n%2)
        n = n//2
    return L[::-1]

def liste(n):
    L = [int(i) for i in str(n)]
    return L
sum = 0
for i in range(10000000):
    if liste(i)==liste(i)[::-1]:
        if binaire(i)==binaire(i)[::-1]:
            sum += i
print(sum)
# 25846868
