# U = I
# N = J
# D = K
# E = l
# X = M
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    if (10*i+j)*(10*i+j) + (10*i+j) == 1000*k+100*l+10*i+m:
                        if i!=j and i!=k and i!=l and i!=m and j!=k and j!=l and j!=m and k!=l and k!=m and l!=m:
                            print(1000*k+100*l+10*i+m)            
                            # 7482
