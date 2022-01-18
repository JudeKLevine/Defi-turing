def carre(a , b):
    Sum = 0
    while b != 0:
        Sum = Sum + a*b
        a = a - 1
        b = b - 1
    return Sum
L = []
for a in range(2, 200):
    for b in range(2, 200):
        if b ‹= a and carre(a, b) == 6400:
            L.append([a, b, a-b])
A = min(L)
print(A[0]*A[1])
# 696
