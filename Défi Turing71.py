def fusion(entier1, entier2):
    List = [i for i in str(entier1)]
    for i in str(entier2):
        List.append(i)
    result = int("".join(List))
    return result
    
def In(entier):
    result = 0
    List = [int(i) for i in str(entier)]
    for i in range(len(List)):
        if List.count(List[i]) == 1 : result += 1
    return result
    
A = [i for i in range(100, 1000) if In(i) == len(str(i))]
for i in A:
    if In(i * i) == len(str(i * i)) and In(fusion(i, i*i)) == 9 and str(i).count('0') == 0: print(i) 
