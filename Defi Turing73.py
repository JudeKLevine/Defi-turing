def liste(n):
    L = [int(i) for i in str(n)]
    return L
A = [i for i in range(1000000, 10000000) if liste(i)==liste(i)[::-1]]
B = [i**2 for i in A if liste(i**2)==liste(i**2)[::-1]]
print(max(B)**0.5)
# 2001002
