for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        if (i*100 + j*10 + k)**2 == l*10000 + m*1000 + 100*n + 10*j + i and i != l:
                            print(l*10000 + m*1000 + 100*n + 10*j + i)
# 28561
