import utilitaire_gen_Q as util_r5

# Q1 Une liste d'employés a été passée dans une variable. 
# Malheureusement les données ont gardé des caractères supplémentaires du fichier original.
# Avant de continuer, imprimez le premier élément de la liste pour voir son contenu. 
# Il devrait ressembler à '01 Ellen Ferguson\\n'
# Faites une boucle qui passe à travers chacun des noms dans la liste.
# La boucle doit :  -retirer le nombre au début de chaque nom
#                   -retirer les charactères "\\n" à la fin de chaque nom
#                   -retirer des espaces superflues au début et à la fin s'il y en a

# Vous n'avez pas besoin des fonctions range() ou len() dans votre boucle.
# Indice : retirer un certain nombre de charactères se fait facilement avec les sous-strings / le slicing

print(f"Q1{80*'_'}")
liste_employee = util_r5.liste_employes
nouvelle_liste = list()





# Q2 Afin de s'assurer de garder un texte facile à écrire, faites un programme qui va prendre du texte en input()
# puis qui va compter la longueur de chaque mot. Il va retourner le nombre de mots de plus de 9lettres ainsi qu'un
# message qui variera :  "Excellent" s'il y a moins de 2 mots dépassant 9 lettres
#                        "Attention au niveau du texte" s'il y a 2 mots et plus
# Vous allez devoir faire un .split() sur le texte obtenu pour avoir chaque mot dans une liste.
print(f"Q2{80*'_'}")
texte = input("Entrez texte : ")





    
#Q3 Cette question est semblable à la question précédante. Mais nous avons 3 messages que nous voulons afficher.
# Nous voulons comptez le nombre de mots dans un texte qui sont de 3 lettres ou moins, entre 4 et 7 lettres inclusivement et plus de 7 lettres.
#Le message imprimez ressemblera à :
#Votre texte contient : X mots de 3 lettres et moins
#                       Y mots de 4 à 7 lettres
#                       Z mots de 8 lettres et plus
# Pour éviter de tester inutilement la longueur, vous DEVEZ absolument utiliser la structure: if...elif...else 
print(f"Q3{80*'_'}")


        
