import os
from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv

import csv
 

# Vous utiliserez encore le fichier "Ex4 Lan Party.csv"
# 
#         Créez une liste des jeux joués dans les différents Lan Party du fichier.
#         N'ajoutez à cette liste chaque jeu qu'une seule fois 
#                         (vérifiez si le jeu est dans la liste avant de l'ajouter
#                          vous pouvez vérifier avec count() combien de fois une valeur est dans une liste
#                          si cette valeur est 0, vous pouvez l'ajouter à la liste)
#         Triez la liste en ordre aphabétique 
#         Finalement, imprimez la liste des différents jeux joués triés en ordre alphabétique


#         Si besoin, des instructions détaillées sont données plus bas

with open("Ex4 lan Party.csv","r",encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    next(csv_reader)
    liste_jeux = []
    for line in csv_reader:
        for game in line[1:]:
            if liste_jeux.count(game) == 0:
                liste_jeux.append(game)
                liste_jeux.sort()
    print(liste_jeux)
            





















# INSTRUCTIONS DÉTAILLÉES
#      Commencez par créer une liste des différents jeux vide
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
#      Sautez la première ligne de l'entête
#      Faites une boucle pour passer à travers chacune des lignes 
#      Utilisez le slicing pour garder uniquement les 3 jeux
#      Faites une boucle pour passer à travers chacun des jeux
#      Avec count, obtenez le nombre de fois que le jeu est dans votre liste des différents jeux
#      Si le count est de 0, vous ne l'avez jamais ajouté alors ajoutez le jeu à votre liste
#      En dehors de toute boucle, utilisez sorted() pour trier la liste et obtenir une nouvelle liste triée
#      Imprimez votre nouvelle liste triée


