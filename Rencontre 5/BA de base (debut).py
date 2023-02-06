# On veut une liste de chiffres
liste_chiffres = [26,35,2,60,60,786]

# On veut une liste de fruits
liste_fruits = ["pomme","raisin","fraise"]

# Pour imprimer chaque élément de la liste de chiffres
for index in liste_fruits:
    print(index)



# Pour imprimer chaque élément de la liste de fruits

for fruits in liste_fruits:
    print(fruits)

    
# Pour avoir le total de tous les chiffres de la liste de chiffres
total = 0
for chiffre in liste_chiffres:
    total += chiffre
print(total)

# Pour avoir le nombre de chiffres dans la liste de chiffres
longeur = len(liste_chiffres)
print(longeur)



# Pour avoir la moyenne de tous les chiffres de la liste de chiffres
moyenne = total / longeur
print(moyenne)

# Pour imprimer seulement les chiffres qui sont supérieurs à 50
for chiffre in liste_chiffres:
    if chiffre > 50:
        print(chiffre)
        
        
        
        
 # Pour compter le nombre de chiffres qui sont supérieurs à 50   
 #      AVANT la boucle: Il me faut penser à créer une variable compteur qui va commencer à 0 
 #      DANS la boucle, si la condition est vraie, je vais augmenter le compteur de 1
 #      APRÈS la boucle, on imprime le résultat
compteur = 0
for chiffre in liste_chiffres:
    if chiffre > 50:
        compteur += 1
print(compteur)



 

 # Pour avoir le total des chiffres qui sont supérieurs à 50   
 #      AVANT la boucle: Il me faut penser à créer une variable total qui va commencer à 0 
 #      DANS la boucle, si la condition est vraie, je vais augmenter ce total de la valeur du chiffre
 #      APRÈS la boucle, on imprime le résultat
total = 0
for chiffre in liste_chiffres:
    if chiffre > 50:
        total += chiffre
print(total)



 

 # Pour avoir la moyenne des chiffres qui sont supérieurs à 50   
 #      AVANT la boucle: 
 #                  Il me faut penser à créer une variable compteur qui va commencer à 0 
 #                  Il me faut penser à créer une variable total qui va commencer à 0 
 #      DANS la boucle, si la condition est vraie,
 #                  je vais augmenter le compteur de 1
 #                  je vais augmenter ce total de la valeur du chiffre
 #      APRÈS la boucle, 
 #                  on calule la moyenne et on imprime le résultat
compteur = 0
total = 0
for chiffre in liste_chiffres:
    if chiffre > 50:
        compteur += 1
        total += chiffre
moyenne = total / compteur
print(moyenne)



  

# Maintenant les f-string sont utiles pour avoir un résultat plus clair.
# On commence par écrire le texte qu'on veut imprimer
# Il y a X chiffres dans la liste et le total est Y
#                            print(f"Il y a X chiffres dans la liste et le total est Y")
# Ensuite on remplace le X par {compteur}  et le Y par {total}

print(f"{compteur} chiffres dans la liste et le total est {total}")