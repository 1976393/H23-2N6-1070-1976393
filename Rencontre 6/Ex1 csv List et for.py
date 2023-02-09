import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# RAPPEL
# dans l'interpréteur de python (dir(str)) #montre ce que fait chacune des méthodes de la classe str#
# dans l'interpréteur de python  dir(str.find) #montre ce que fait la méthode find de la classe str# 


# Importez csv


 

# Regardez le contenu du fichier "Ex1 Emplois Reseautique.csv"
# 
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                   Poste;Compagnie;Ville;Expérience;Diplôme;Salaire
#          Certains champs ont la valeur "Non déterminé"
#          C'est souvent pour ne pas passer à côté de candidats intéressants. Ils sont souvent ouverts à engager de jeunes diplomés

#          Il vous faudra imprimer les informations des emplois demandant le Diplôme de 'Dec' ou ayant la valeur 'Non déterminé'
# 
#  Si vous êtes à l'aise en programmation allez-y
#  Des instructions détaillées sont données plus bas



























# INSTRUCTIONS DÉTAILLÉES
# Ouvrez en lecture le fichier "Ex1 Emplois Reseautique.csv", en utilisant l'encoding utf-8   
# Lisez tout le contenu du fichier avec csv.reader() avec le delimiter=';'  

# Sautez la première ligne avec next() puisqu'elle ne contient que les entêtes de colonnes
# Dans votre boucle qui passera à travers les lignes
#      ATTENTION chaque ligne d'un fichier csv est une liste
#     (on n'a pas de split à faire ensuite , le csv.reader le fait pour nous et nous retourne une liste des parties de la ligne
#      Le diplôme sera l'élément à l'indice 4 
#      Vérifiez sa valeur et si elle est 'Dec' ou 'Non déterminé' imprimez l'offre d'emploi
#        

        
