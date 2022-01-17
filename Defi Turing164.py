def retire0(n):
    L = [i for i in str(n) if i != '0']
    L = "".join(L)
    return int(L)
a = 0
for i in range(404, 100000):
    if retire0(i) == i/9: 
        a = a + i
print(a)
# 170505
