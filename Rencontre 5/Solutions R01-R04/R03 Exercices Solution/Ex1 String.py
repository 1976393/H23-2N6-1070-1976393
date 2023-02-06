
# Pour chaque question ci-dessous, faites le code demandé puis imprimez toujours 80*'_' afin de séparer les questions.      #
# Imprimez le résultat en utilisant f-string pour afficher le numéro de la question et les infos demandées                  #



# Q1                                                                                                                   #
# Vous avez ici une liste de différents processeurs            
# Vous pouvez aussi mettre un autre modèle de carte graphique si vous voulez.#
# imprimez la liste                                                                                                    #
# Changez la liste en une chaine de caractères avec les cartes graphiques séparées par des virgules
processeurs = ['AMD Ryzen 9 5950X', 'AMD Ryzen 9 5900X', 'AMD Ryzen 7 5800X3', 'Intel Core i9 12900 K', 'Intel Core i7 12700 K', 'Intel Core i5 12600 K']
print(f"Q1: Voici la liste des processeurs: {processeurs}")
str_processeurs = ", ".join(processeurs)
print(f"    Et voici la liste transformée en une chaine de caractères:.\n    {str_processeurs}")
print(80*'_' )


#Q2                                                                                                                   #
#  Voici une chaine de caractères qui ressemble à une ligne de données que vous auriez extraite d'un fichier text     #
ligne_donnees = " AMD Ryzen 9 5900X ;  AMD Ryzen 7 5800X3 ;  Intel Core i9 12900 K    "                               #
#  Vous devez dans un premier temps séparer les données sur le caractère qui les séparent
#  Vous voulez ensuite avoir une liste de chacun des processeurs sans les espaces avant et après chaque processeur processeurs                                                                                            #
#  Imprimez la liste maintenant                                                                    #
list_donnees = ligne_donnees.split(';')
for donnee in list_donnees:
    donnee.strip()
print(f"Q2: liste des données arrangées  {list_donnees}")
print(80*'_' )


# Q3                                                                                                                   #
# Voici un nom de fichier dont chaque partie est séparée par un _                                                      #
nom_fichier_et_extension = "Python_Rencontre 3_Approfondissement str.docx"                                             #
# Séparez nom_fichier_et_extension sur le '.' et gardez les parties dans des sous-chaines séparées                     #
nom_fichier, extension  = nom_fichier_et_extension.split('.')                                                          #
# Séparez le nom de fichier de façon à récupérer le nom du cours, la rencontre et le sujet de la rencontre             #
cours, rencontre, sujet= nom_fichier.split('_')
# Imprimez le nom du cours, la rencontre et le sujet de la rencontre                                                   #
print(f"Q3: Dans ce cours {cours}, la {rencontre} sera sur {sujet}")
print(80*'_' )

#Q4
#  remplir un string pour qu'il fasse 2 caractères de long avec .zfill
#  Au départ, vous avez une chaine qui contient des nombres
str_nombres = "1,5,10,15,20,25"
#  transformez cette chaine en une liste
liste_nombres = str_nombres.split(',')
#  triez cette liste en nombres croissants tout en conservant la liste de nombres originale (avec sorted)
liste_nombres_triee = sorted(liste_nombres)
# Imprimez la liste. Qu'est-ce qui est étonnant?
print(liste_nombres_triee)
# Pour pouvoir avoir la liste de string dans un ordre croissant numérique il faut remplir les valeurs pour qu'ils soient tous 2 de long
for index in range(len(liste_nombres)):
    liste_nombres[index] = liste_nombres[index].zfill(2)
   
liste_nombres_triee = sorted(liste_nombres)
print(liste_nombres_triee)
print(80*'_' )



