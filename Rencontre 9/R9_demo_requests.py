# comment intaller un module qu'on n'a pas déjà installé dans python
# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/
# Dans le terminal              pip install requests

# Fake Store REST API
import requests
import json

BASE_URL = 'https://fakestoreapi.com'
# lien vers la doc :  https://fakestoreapi.com/docs


# faire une demande de tous les produits (GET)



#######################################################################
# pour avoir seulement quelques produits
# l'API nous offre /products?limit=x

# faire une demande de 3 produits (GET/products?limit=3)





######################################################################
# pour avoir un produit précis
# l'API nous offre /products/productID

# faire une demande pour le produit dont l'id est 18 (GET/products?18)







######################################################################
# Une fois la réponse obtenue, on peut convertir la réponse en objet python et les utilisés
# si on veut trier les produits selon leurs catégories





######################################################################
# Ou bien si on veut extraire les noms des tous les clients et les mettres dans une liste.







######################################################################
# Ou encore, on peut aller chercher les produits dans un panier puis aller chercher chacun de ces produits










######################################################################
######################################################################
# Si on fait une requête à un autre API, il faut regarder la doc
# https://fakerapi.it/en


BASE_URL = "https://fakerapi.it/api/v1/"



# donc si on veut obtenir les 10 premières adresses




# Avec cette API, les résultats sont aléatoires par défaut.
# Allons chercher les mêmes trois livres de facon reproduisable