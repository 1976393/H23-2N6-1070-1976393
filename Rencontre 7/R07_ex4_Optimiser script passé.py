import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script


# importez les packages os et csv #
import os
import csv



#  On pourrait découper ce script en plusieurs fonctions pour que cela soit plus clair ce qui est fait 

#  une fonction qui va avoir le nom du fichier en paramètre
# 		qui va lire le nom du fichier , en extraire le cours et le groupe et qui retourne ces deux infos avec un "/"
#       donc ici "4201B3/gr1010"
#  une fonction qui va avoir le nom du fichier en paramètre
#       qui va lire les données du fichier et retourner une liste des étudiants avec leur nom prenom

#  Le programme principal sera d'appeler ces fonctions puis de créer les répertoires désirés
#  Votre code devrait toujours fonctionner

def extraire_cours_groupe(fichier):
	fichier_nom = fichier.split("_")
	cours = fichier_nom[2][5:]
	groupe = fichier_nom[3][:6]
	return(f"{cours}/{groupe}")

def obtenir_Liste_etudiants(full_f_name):
	noms_Etudiants=[]
	with open(full_f_name,'r') as data_CSV:
		csv_data = csv.reader(data_CSV,delimiter=';')
		# sauter la première ligne #
		next(csv_data)
		for line in csv_data:
			noms_Etudiants.append(f"{line[2]} {line[3]}")
	return noms_Etudiants

full_f_name = "Ex4_ListeEtudiants_cours4201B3EM_gr1010.csv"         
cours_groupe = extraire_cours_groupe(full_f_name)
noms_Etudiants = obtenir_Liste_etudiants(full_f_name)
os.makedirs(cours_groupe)
os.chdir(cours_groupe)
for item in noms_Etudiants:        
    os.mkdir(item)
    





    
# def nom_fichier(fichier):
#     fichier = "Ex4_ListeEtudiants_cours4201B3EM_gr1010.csv".split("_")
#     cours = fichier[2][5:]
#     groupe = fichier[3][:6]
#     return(f"{cours}/{groupe}")

# print(nom_fichier("Ex4_ListeEtudiants_cours4201B3EM_gr1010.csv"))

# def 