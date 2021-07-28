def nbr_irr(n):
    A = [int(i) for i in str(n)]
    sum = 0
    for i in A :
        if i != 0 and n % i == 0:
            sum += 1
    return sum
    
A = [i for i in range(10,1000000) if nbr_irr(i) == 0]

print(len(A))
