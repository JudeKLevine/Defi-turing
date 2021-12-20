def suite(n):
    if n == 0 : return 0
    if n == 1 : return 1
    if n%2 == 0 : return suite(n//2)
    else : return suite((n-1)//2) + suite((n-1)//2 + 1)
print(suite(10000001))
# 9469
