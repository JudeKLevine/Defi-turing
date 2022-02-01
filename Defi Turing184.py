def nbr_occ(lettre):
    S = [lettre.count(i) for i in lettre]
    a = sum(S)
    if a == len(S): return 1
    else : return 0
A = 0
with open("C:/Users/dico.txt", encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.replace("é","e")
        ligne = ligne.replace("è","e")
        ligne = ligne.replace("ê","e")
        ligne = ligne.replace("-","")
        A += nbr_occ(ligne)
print(A)*
# 29488
