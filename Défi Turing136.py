for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    if i!=j and i!=k and i!=l and i!=m and j!=k and j!=l and j!=m and k!=l and k!=m and l!=m:
                        if (10 * i + j) * k == 10 * l + m and i < j < k < l < m:
                            print(10000 * i + 1000 * j + 100 * k + 10 * l + m)
