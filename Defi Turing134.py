L = 0
for i in range(12, 100):
    for j in range(12, 100):
        a = int(str(i)[::-1])
        b = int(str(j)[::-1])
        if (i*i - j*j)//1000 == 5 and a*a - b*b == i*i - j*j and i%11!=0 and j%11!=0:
            L = L + a*a - b*b
print(L//2)
# 11453
