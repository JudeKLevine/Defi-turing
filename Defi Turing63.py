sum = 0
for i in range(1000):
    for k in range(50):
        if len(str(i**k))==k:
            print(i**k)
            sum += 1
print(sum-1)
# 49
