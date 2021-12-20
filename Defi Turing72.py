Sum = 0
for i in range(10,31624):
    a = len(str(i*i))
    if str(i*i)[a-3:a] == '444':
        print(i*i)
        Sum = Sum + 1
print(Sum)
# 127
