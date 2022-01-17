def liste(n):
    L = [int(i) for i in str(n)]
    return L
A = [2*i for i in range(10000)]
B = [A[i]*A[i+1]*A[i+2] for i in range(9998)]
for i in B:
    if liste(i)==liste(i)[::-1]:
        print(i)
 # 8488848
