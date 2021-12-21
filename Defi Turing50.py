L = []
for i in range(40):
    for j in range(40):
        for k in range(40):
            L.append(2**i * 3**j * 5**k)
L.remove(1)
L.sort()
print(L[2012])
# 8542968750
