import utilitaire_gen_Q as util_r5
# Q1 Ce petit script demande l'âge de la personne et imprime sa date de naissance.
# La fonction input() retourne une valeur en string.
# Ajouter un test conditionnel sur l'input qui :
#                      -imprime "ERREUR - âge non-valide" si la valeur entrée n'est pas un chiffre entier 
#                      -et qui convertie l'input en int si possible. 
# Indice : pour pouvez utiliser la fonction  dir(str)  pour obtenir toutes les méthodes
# des objets str... une de ces méthodes devrait vous aider... vous ne trouverez pas la méthode exact dans vos notes de cours. 
print(f"Q1{80*'_'}")
age = input("Entrez votre age : ")




print(util_r5.annee_de_naissance(age)) # imprime l'année de naissance si age est bien un int.



# # Q2 Des variables sont générés par une fonction dans un module utilitaire.
# # Imprivez la valeur de chaque variable et son type
print(f"Q2{80*'_'}")
var1,var2,var3,var4,var5,var6 = util_r5.generation_variable()



#