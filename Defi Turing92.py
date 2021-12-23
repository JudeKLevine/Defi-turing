a = 0
result = []
for i in range(2,1000):
  a = a  + i - 1 
  for j in range(1007):
    if i*j + a == 2014 : result.append(j)
produit = 1
for i in result:
  produit = produit*i
print(produit)
# 584328
