from random import *

# liste principale
liste1=[1,2,3,4]
liste2=[1,2,3,4]
n1 = choice(liste1)
n2 = choice(liste2)

# listes de comparaison pour savoir 
# s'il saisie un chiffre suppérieur au résultat
listCP1=[1,3,4,5]
listCP2=[1,3,4,5]
p1 = choice(listCP1)
p2 = choice(listCP2)

# listes de comparaison pour savoir 
# s'il saisie un chiffre suppérieur au résultat
listCM1=[1,3,4,5]
listCM2=[1,3,4,5]
m1 = choice(listCM1)
m2 = choice(listCM2)

# différents opération de soustraction pour trouver
#  les nombres de prés de 1 du résultat
sum_list1 = []
for (item1, item2) in zip(liste1, listCP1):
    sum_list1.append(item1-item2)
sum_list2 = []
for (item1, item2) in zip(liste2, listCP2):
    sum_list1.append(item1-item2)
sum_list3 = []
for (item1, item2) in zip(liste1, listCM1):
    sum_list1.append(item1-item2)
sum_list4 = []
for (item1, item2) in zip(liste2, listCM2):
    sum_list1.append(item1-item2)

print(n1,n2)

x = input("entre les coordonees en absice ou vous pensez que le bateau se trouve: ")
y = input("entre les coordonees en ordonee ou vous pensez que le bateau se trouve: ")

while (x,y) != (n1,n2):
    print("Dans l'eau !")
    x = input("entre les coordonees en absice ou vous pensez que le bateau se trouve: ")
    y = input("entre les coordonees en ordonee ou vous pensez que le bateau se trouve: ")
    print(x,y)

if (x,y) == (sum_list1,sum_list2):
        print("Pas loin! reessaye")
elif (x,y) == (n1,n2):
    print("Touche, coule: Tu as gagne !")