def nbr_occ(lettre):
    S = [1 for i in lettre if lettre.count(i) == 2 ]
    a = sum(S)
    if a == len(lettre): return 1
    else : return 0

fichier = open("C:/Users/Jude/Desktop/dico.txt","r")
res = 0
contenu = fichier.read()

for ligne in contenu.split():
    ligne = ligne.replace("é","e")
    ligne = ligne.replace("è","e")
    ligne = ligne.replace("ê","e")
    ligne = ligne.replace("-","")
    res += nbr_occ(ligne)
    
print(res)
# 171


