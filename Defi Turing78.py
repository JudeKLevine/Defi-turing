for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if 1000*i + 100*j + 10*k + l == i**j * k**l:
                    print(1000*i + 100*j + 10*k + l)
# 2592
