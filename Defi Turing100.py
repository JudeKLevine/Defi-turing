def premier(n):
    Sum = 0
    for i in range(2,n//2 + 1):
        if n%i == 0:
            Sum = Sum + 1
    return Sum
L = [i for i in range(2,100) if premier(i) == 0]
for i in L:
    for j in L:
        for k in L:
            for l in L:
                for m in L:
                    for n  in L:
                        if i+j+7 == 1+k+l and 1+k+l == m+13+n and i+1+m==j+k+13 and j+k+13==7+l+n and i+k+n==m+13+n:
                            print(i*k*m)
                            # 106597
