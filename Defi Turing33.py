# Retrouver ce algorithme sur wikipedia
# https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques

def dimanche_paques(annee):
    
    n = annee%19
    c = annee//100
    u = annee%100
    q = (c - ( (c+8)//25 ) + 1)//3
    e = (19 * n + c - c//4 - q + 15)%30
    L = (2 * ( c%4 ) + 2 * ( u//4 ) - e - ( u%4 ) + 32 )%7
    m = (e + L - 7 * ( (n + 11 * e + 22 * L)//451 ) + 114)//31
    j = (e + L - 7 * ( (n + 11 * e + 22 * L)//451 ) + 114)%31
    
    return m,j

a = 0
for i in range(2001, 10000): 
    if dimanche_paques(i)[0] == 4: a += 1
print(a)
# 6119
