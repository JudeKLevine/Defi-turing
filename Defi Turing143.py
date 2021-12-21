def count5(n):
    a = 0
    for i in range(n + 1):
        if str(i).count('5') > 0:
            a = a + 1
    return a
for i in range(1000000, 9999999):
    if(count5(i) == i//2:
        print(i)
# 5314408
