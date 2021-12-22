def liste(n):
    A = [int(i) for i in str(n)]
    return A
def test(L,M):
    sum = 0
    for i in L:
        if i in M:
            sum += 1
            M.remove(i)
    return sum
        
for i in range(100000,1000000):
    if len(liste(i))==len(liste(2*i))==len(liste(3*i))==len(liste(4*i))==len(liste(5*i))==len(liste(6*i)):
        if test(liste(i),liste(2*i))==len(liste(i)) and test(liste(2*i),liste(3*i))==len(liste(i)) and test(liste(3*i),liste(4*i))==len(liste(i)) and test(liste(5*i),liste(4*i))==len(liste(i)) and test(liste(5*i),liste(6*i))==len(liste(i)):
            print(i)
  # 142857
