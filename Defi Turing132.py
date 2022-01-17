a = 0
for i in range(54772): # 2x²+3x+1=6*10^9
    if (2*i+1)*(i+1)%6 == 0:
        a = a + 1
print(a)
# 18257
