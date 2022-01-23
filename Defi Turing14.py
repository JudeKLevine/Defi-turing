def syracuse(n):
    sum = 1
    while n != 1:
        if n%2 == 0:
            n = n//2
            sum  += 1
        else:
            n = (n*3+1)
            sum += 1
    return sum
max = [0,0]
for i in range(1100000,1200000):
    if syracuse(i)>=max[0]:
        max[0], max[1]=syracuse(i), i
print(max)
# 1117065
