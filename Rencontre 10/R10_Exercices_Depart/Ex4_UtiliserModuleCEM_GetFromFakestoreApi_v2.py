# importez le module v2 que vous avez fait pour obtenir des données de différents type de FakestoreApi
import Ex3_CEM_GetFromFakestoreApi_v2 as v2




# Q1 A Utilisez la méthode request_from de votre module pour obtenir 3 produits
ls_produits = v2.request_from("products",3)

#           Commencez par imprimer la liste des trois produits 
#                   puis voyez la clé qui vous permettra d'obtenir le nom du produit


# Q1 B Imprimez la liste des noms de ces trois produits 

for item in ls_produits:
    print(item["title"])




print(80*'_')
# Q2 A Utilisez la méthode request_from de votre module pour obtenir 1 cart 


#           Commencez par imprimer la liste du cart obtenu
#                   puis voyez la clé qui vous permettra d'obtenir la liste des produits dans le cart

# Q2 B Imprimez le nombre de produits qu'il y a dans ce cart





print(80*'_')


# Q3 Finalemnet, essayez d'uilisez la fonction request_from de votre module pour obtenir un objet du type bonbon

