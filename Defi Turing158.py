def somme_cube(n):
    L = [int(i)*int(i)*int(i) for i in str(n)]
    return sum(L)
    
def Suite(n):
    a = n
    L = []
    b = 0
    while L.count(153) == 0 and b < 200: # Nbr interation < 200
        L.append(a)
        a = somme_cube(a)
        b = b + 1
    if b == 200 :  return 0
    else : return n
L = []
for i in range(2001, 3001):
   L.append(Suite(i))
print(sum(L))
# 835167
