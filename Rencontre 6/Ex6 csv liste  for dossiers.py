import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv

import csv
 

# Vous utiliserez encore le fichier "Ex4 Lan Party.csv"
# 
#         Vous voulez créer un dossier par Lan Party
#         Et pour chaque Lan Party, créez des sous-dossier pour chaque jeu
#                   (On y mettra éventuellement la liste des participants du Lan qui veulent jouer à ce jeu)
#         ATTENTION: Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères

#         Si besoin, des instructions détaillées sont données plus bas

with open("Ex4 lan Party.csv","r",encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    path = os.getcwd()
    next(csv_reader)
    for line in csv_reader:
        os.mkdir(f"{path}/{line[0]}")
       
        for folders in range(1,len(line)):
            os.chdir(f"{path}\\{line[0]}\\")
            new_path = os.getcwd()
            os.mkdir(f"{new_path}\\{line[folders][:20].replace(':', '_')}")



















# INSTRUCTIONS DÉTAILLÉES
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
#      Sautez la première ligne de l'entête
#      Faites une boucle pour passer à travers chacune des lignes 
#      Créez un dossier pour le nom du Lan Party
#      Déplacez vous dans ce dossier
#           Utilisez le slicing pour garder uniquement les 3 jeux
#           Faites une boucle pour passer à travers chacun des jeux
#                   Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères
#                   Créez un dossier pour le jeu avec le nouveau nom de jeu
#           Revenez au dossier parent
