# importez le module que vous avez fait pour obtenir des données de différents types de FakestoreApi
import Ex1_CEM_GetFromFakestoreApi_v1 as req



# Q1  Il faut dans un premier temps tester les cas limites des fonctions que vous avez faites dans votre module
# Passer 1 en paramètre
# Passer 10 en paramètre
# Passer -1 en paramètre
# Passer 11 en paramètre



# Utilisez la méthode request_carts de votre module en passant 1 en paramètre
req.requests_carts(1)



print(80*'_')
# Utilisez la méthode request_carts de votre module en passant 10 en paramètre
req.requests_carts(10)



print(80*'_')
# Utilisez la méthode request_carts de votre module en passant -1 en paramètre
req.requests_carts(-1)



print(80*'_')
# Utilisez la méthode request_carts de votre module en passant 11 en paramètre
req.requests_carts(11)



print(80*'_')










print(80*'_')
# Q2 A   Utilisez la méthode request_products de votre module pour obtenir 3 produits
req.request_products(3)


#           Commencez par imprimer la liste des trois produits 
#                   puis voyez la clé qui vous permettra d'obtenir le nom du produit



print(80*'_')
# Q2 B Imprimez la liste des noms de ces trois produits 
ls_produits = req.request_products(3)
for item in ls_produits:
        print(item["title"])



print(80*'_')
# Q3 A   Utilisez la méthode request_carts de votre module pour obtenir 1 cart 
ls_carts = req.requests_carts(1)
print(ls_carts)


#           Commencez par imprimer la liste du cart obtenu
#                   puis voyez la clé qui vous permettra d'obtenir la liste des produits dans le cart



# Q3 B   Imprimez le nombre de produits qu'il y a dans ce cart
for item in ls_carts:
        print(item["products"])





print(80*'_')


# Q4 A Utilisez la méthode request_carts de votre module pour obtenir 6 carts
ls_carts6 = req.requests_carts(6)


# Q4 B Pour chaque cart id, imprimez le nombre de produits de ce cart 
for carts in ls_carts6:
        print(carts["products"])