from math import factorial as fact
def ter(n):
    sum, i = 0, 0
    A = [int(i) for i in str(n)][::-1]
    while A[i]==0:
        i     += 1
        sum   += 1
    return sum
  print(ter(100000000))
  # 24999999
