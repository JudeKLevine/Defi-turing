def liste(n):
    L = [int(i) for i in str(n)]
    return L
def miror(n):
    L = [str(i) for i in liste(n)][::-1]
    L="".join(L)
    return int(L)
A = [i for i in range(10000,31624)]
B = [i for i in A if i**2==miror(miror(i)**2)]
print(B[-1]**2)
# 967894321
