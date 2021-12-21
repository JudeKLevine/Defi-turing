def liste(n):
    L = [int(i) for i in str(n)]
    return L

A = [i for i in range(4000000) if liste(i*i)==liste(i*i)[::-1]]
print(sum(A))
# 27974694
