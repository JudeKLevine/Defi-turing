def T(n):
    return n*(n+1)/2
def t(n):
    return int((n*(n+1)*(2*n + 1))/12 + n*(n+1)/4)
L = [T(i) for i in range(9000)]
B = [t(i) for i in range(9000)]
Max = 0
for i in B:
    if i in L and i > Max:
        Max = i
print(Max)
# 7140
