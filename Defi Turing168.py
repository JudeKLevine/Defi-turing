def P_ou_I(n):
    P = ['0','2','4','6','8']
    I = ['1','3','5','7','9']
    a = 0
    Char = str(n)
    if Char[0] in P:
        for i in Char:
            if i in P: a = a + 1
    if Char[0] in I:
        for i in Char:
            if i in I : a = a + 1
    if a == len(Char): return 1
    else : return 0
a = 0
for i in range(1000):
    if P_ou_I(i*i) == 1 : 
        a = a + i*i
print(a)
#6589122
