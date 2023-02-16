import datetime


employe = {"prenom":"Ana","nom":"tremblay","departement":"informatique","id":732,"equipe":"Team C"}


# On veut obtenir le nom complet de l'employé
# nom_complet = f'{employe["prenom"]} {employe["nom"]}'
# print(nom_complet)

# Déja, on se rend compte d'une erreur lorsque le nom a été entré
# on veut que le nom de famille commence par une majuscule.
nom_corrige = employe["nom"]
nom_corrige = nom_corrige.capitalize()

employe["nom"] = nom_corrige

nom_complet = f'{employe["prenom"]} {employe["nom"]}'
print(nom_complet)
print(employe)

# Maintenant, on veut vérifier la date d'embauche de l'employé. 
# S'il n'y a pas de date c'est un nouvel employé dont le dossier n'est pas encore terminé.

#print(employe["date_embauche"])
if not employe.get("date_embauche") :
    employe["date_embauche"] = datetime.date.today().isoformat()
print(employe)


# On veut retirer la clef "equipe" du dictionnaire car il s'agit d'un vestige d'un ancien système dans la compagnie
# Pourquoi pop() plutot que del ?
# del employe["equipe"]


element_retirer = employe.pop("equipe")
print(employe)
print(f"L'élément équipe avec une valeur {element_retirer} a été retiré")


# Dans ces exemples nous travaillons avec un dictionnaire que nous connaissons.
# Si on travaille avec un dictionnaire qu'on a obtenu à partir d'une source externe...
# il faut d'abord connaitre les clefs.

clef = employe.keys()

print(clef)


# On peut aussi travailler avec chacune des paires celf:valeur une après l'autre.
for clef, valeur in employe.items():
    print(clef, valeur)

# # Maintenant, on veut ajouter une liste des langagues de programmation connus par l'employe pour savoir quel cours il pourrait donner.
competences = ["Python","C#","Pascal","Assembleur","Fortran","Magic the gathering"]
employe["language"] = competences
print(employe)


# # Si ensuite on veut extraire les languages pour une raison quelconque
print()
print(employe["language"][0])


# # La clef "languages" du dictionnaire "employe" correspond réellement à une liste.
# # Toutes les méthodes et particuliarité des listes sont utilisables.
# # Si on veut uniquement le premier language...




# # Si on veut ajouter un language

employe["language"].append("Ruby")
print(employe["language"])



# Maintenant que nous avons fini de travailler sur le nouvel employe, 
# nous allons ajouter le dictionnaire contenant ses informations à une liste de tous les employées

liste_employés_2023 = [ {"prenom":"Bob","nom":"Uvoy","departement":"informatique","id":645,"languages":["C#","C++","C","Java"]},
                        {"prenom":"Chris","nom":"Volaire","departement":"informatique","id":987,"languages":["Ruby","Java","Perl"]},
                        {"prenom":"Edouard","nom":"Petit","departement":"multimédia","id":258,"languages":["C#"]}]

print(type(liste_employés_2023))

liste_employés_2023.append(employe)
# print(liste_employés_2023)



print("Bienvenu aux nouveaux employés de 2023 :")
for personne in liste_employés_2023:
    print(f'\t{personne["prenom"]} {personne["nom"]}',end="")
    if personne == liste_employés_2023[-1]:
        print("  !")
    else:
        print(",")