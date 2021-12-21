a = 1
b = 13
c = 169
d = 2014
result = 0
for i in range(2010):
    result = d
    d = a + b + c + d
    a = b
    b = c
    c = result
print(len(str(d)))
# 576
