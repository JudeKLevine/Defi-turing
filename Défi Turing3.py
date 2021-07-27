def decomposition(entier):
    Liste = []
    for i in range(2,entier):
        while entier % i == 0:
            entier = entier // i
            Liste.append(i)
    return Liste
    
print(decomposition(20130101)[-1])
