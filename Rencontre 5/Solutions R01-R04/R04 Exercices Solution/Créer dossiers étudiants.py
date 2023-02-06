# importez les packages os et csv #
import os
import csv


# dans ce script vous allez faire les étapes suivantes:
#   - créez une variable qui va contenir le nom du fichier csv à lire, soit ici 'ListeEtudiants_cours4201B3EM_gr1010.csv'
#   - utilisez split pour obtenir le nom du ficher 
#   - utlisez find pour trouver l'index de '420'
#   - utilisez le slicing pour extraire le cours, soit les 6 caractères après le début de l'index que vous venez de trouver 
#   - utilisez find pour trouver l'index de 'gr'
#   - utilisez le slicing pour extraire le groupe, soit les 6 caractères après le début de l'index que vous venez de trouver 
#   - créez maintenant le dossier pour le cours. puis dans ce dossier le dossier pour le groupe
#   - créez une liste vide qui contiendra les noms des étudiants
#   - ouvrez le fichier en lecture avec pour delimiter le ;
#   - sautez la première ligne qui contient les en-têtes 
#   - Ajoutez les noms et prénoms des étudiants qui sont dans le fichier dans votre liste des étudiants
#   - Déplacez vous dans l'arborescence des dossiers pour aller dans le dossier du groupe que vous avez créé
#   - Finalement faites une boucle pour créer un dossier avec les noms et prénoms que vous avez dans votre liste.

# full_f_name = 'ListeEtudiants_cours4201B3EM_gr1010.csv'
# f_name, f_ext = full_f_name.split('.')
# index_cours = f_name.find('420')
# cours = f_name[index_cours:index_cours+6]
# index_groupe = f_name.find('gr')
# groupe = f_name[index_groupe:index_groupe+6]

# os.makedirs(cours+'/'+groupe)
# dir_depart = input("Entrez le chemin vers le répertoire de départ: ")
dir_depart = 'F:\FC\Cohorte no 1_ Gr6301\BD5 20230123 au 20230407\Suivi étudiant\TP_R1'
os.chdir(dir_depart)

sigle_cours = input("Entrez le sigle du cours (420BD5): " )
groupe = input("Entrez le no du groupe (6301): ")

os.mkdir(groupe)

file_to_open = f'ListeEtudiants_cours{sigle_cours}EM_gr{groupe}.csv'
noms_Etudiants = []

with open(file_to_open,'r') as data_CSV:
    csv_data = csv.reader(data_CSV,delimiter=';')
      #sauter la première ligne #
    next(csv_data)
    for line in csv_data:
        nom_famille = line[2][1:].strip('"')
        prenom = line[3][1:].strip('"')
        noms_Etudiants.append(f"{nom_famille} {prenom}")

print(noms_Etudiants)
# dir_desire = input("Entrez le répertoire désiré")
# sousdir_desire = input("Entrez le sous-répertoire désiré")
# le_chemin = os.path(dir_desire,sousdir_desire)
# os.makedirs(le_chemin)
# os.chdir(le_chemin)
os.chdir(groupe)
for item in noms_Etudiants:        
    os.mkdir(item)
