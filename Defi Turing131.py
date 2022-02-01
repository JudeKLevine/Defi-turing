import numpy as np
import matplotlib.pyplot as plt
def tri(a):
    x = a[1]
    return x

def inv(n):
    return int(str(n)[::-1])

s = 0
a = 0
for i in range(1000000):
    a += inv(i)
    
    if a < (i*(i+1))/2: s += i
print(s)
# 97118501919
