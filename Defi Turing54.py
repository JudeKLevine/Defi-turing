L = []
for i in range(10):
    for j in range(1000):
        for k in range(100):
            if ((10000*i + 2*1000 + j)*(k))//100 == 2222 :
                L.append([10000*i + 2*1000 + j, k,(10000*i + 2*1000 + j)*(k) ])
B = [i[0] for i in L if str(i[0]).count('2') == 1 and str(i[1]).count('2') == 0 and str(i[2]).count('2') == 4]
print(max(B)) 
# 12348
