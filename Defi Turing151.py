for i in range(150):
    for j in range(150):
        for k in range(150):
            if i**2 == j**2 + k**2 and (j*k)/2 == 2016 and i>j>k:
                print(int(str(k)+str(j)+str(i)))
# 32126130           
