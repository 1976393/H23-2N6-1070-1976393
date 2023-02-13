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

def extraire_cours_groupe(full_f_name):
	f_name, f_ext = full_f_name.split('.')
	index_cours = f_name.find('420')
	cours = f_name[index_cours:index_cours+6]
	index_groupe = f_name.find('gr')
	groupe = f_name[index_groupe:index_groupe+6]
	return cours+'/'+groupe

def obtenir_Liste_etudiants(full_f_name):
	noms_Etudiants=[]
	with open(full_f_name,'r') as data_CSV:
		csv_data = csv.reader(data_CSV,delimiter=';')
		#sauter la première ligne #
		next(csv_data)
		for line in csv_data:
			noms_Etudiants.append(f"{line[2]} {line[3]}")
	return noms_Etudiants

full_f_name = 'Ex4_ListeEtudiants_cours4201B3EM_gr1010.csv'         
cours_groupe = extraire_cours_groupe(full_f_name)
os.makedirs(cours_groupe)
os.chdir(cours_groupe)
noms_Etudiants = obtenir_Liste_etudiants(full_f_name)
for item in noms_Etudiants:        
    os.mkdir(item)
