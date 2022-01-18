a, b = 1, 1
sum = 0

for i in range(100):
    a, b = b, a + b
    if a % 2 == 1 and a < 4000000:
        sum += a
print(sum)
# 4613732
