for k in range(25, 117):
    for j in range(25):
        a = 0
        for i in range(1+j, 26+j):
            if k/i ‹= 5 and k/i >= 2:
                a = a + 1
        if a == 25:
            print(k, 1+j, 26+j)
# 80
