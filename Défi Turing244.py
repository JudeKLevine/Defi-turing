def somme_cube(entier):
    List = [int(i) * int(i) * int(i) for i in str(entier)]
    return sum(List)
    
def lenght_suite(entier):
    a = entier
    List = []
    while List.count(a) == 0:
        List.append(a)
        a = somme_cube(a)
    return len(List) +1

max = 0
indice = 0
for i in range(1000000):
    if lenght_suite(i) > max:
        max = i
print(max)
