# comment intaller un module qu'on n'a pas déjà installé dans python
# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/
# Dans le terminal              pip install requests

# fakerapi.it/en
from textwrap import indent
import requests
import json

BASE_URL = 'https://fakerapi.it/api/v1'


# pour avoir seulement X produits
# l'API nous offre /products?_quantity=X

# Q1)   faire une demande de 1 produit1 (GET/products?_quantity=1) et conservez le résultat dans une variable

answer = requests.get(f'{BASE_URL}/products?_quantity=1')

print(answer)


# json.dump permet d'ajouter des arguments
# indent pour spécifier le niveau d'imbrication des éléments de la réponse
# et que ce soit plus facile à comprendre la structure de la réponse

# Q2)  faites un dumps de la réponse obtenue en Q1 avec un niveau d'indentation de 4  et conservez le résultat dans une variable
texte_string = json.dumps(answer.json(),indent=4)
print(texte_string)

# Q3)  Le résultat obtenu en Q2 est un string et doit être changé en un dictionnaire avec json.load  et conservez le résultat dans une variable
# using json.loads() method
texte_indent = json.loads(texte_string)
print(texte_indent)

#Si je regarde seulement ce qui m’intéresse
#dict_resultat = {
#             "data": [       
#             {
#                "id": 1,
#                "name": "Blanditiis aut in quia omnis.",
#                 "net_price": 2.15,
#                 "taxes": 22,
#                "price": "2.62",
#                 "categories": [
#                     2,
#                     3,
#                     5
#                 ],
#             }
#             ]
#        }


# Donc, dict_resultat est un dictionnaire. La clé "data" me donne une liste. Qui n'a qu'un seul item pour le moment

#  dict_resultat["data"][0]  me donnerais un dictionnaire contenant les infos du produit
# #                            avec l'id, le name,..et le price que je recherche, ainsi qu'une liste de categories

#  Pour le moment, avec un produit, je peut obtenir le 'price' du produit et vérifier s'il est dans la catégorie 3.

# Q4)  Obtenez le premier élément du dictionnaire avec la clé 'data' dans une variable
data = json.loads(requests.get(f'{BASE_URL}/products?quantity=1').text)
print("_"*80)
print(data['data'][0])
#print(json.dumps(data,indent=4))

#  Donc on obtient quelque chose comme
# {'id': 1, 'name': 'Blanditiis aut in quia omnis.', 'net_price': 2.15, 'taxes': 22, 'price': '2.62', 'categories': [2, 3, 5]}

#  Q5) Obtenez le prix et changez le en un float
prix = float(data['data'][0]["price"])
print(prix)

#  Q6)  Utilisez in pour vérifier si 3 fait partie des categories du dictionnaire des categories du produit
#for num in data["data"][0]["categories"]:
if 3 in data["data"][0]["categories"]:
    print("true")
#  Q7)  Imprimez le prix et si le produit est dans la catégorie 3 ou non
#       Quelque chose comme: "Le produit a le prix de 3945.01 et on peut savoir s'il est dans la catégorie 3: False"
if 3 in data["data"][0]["categories"]:
    print(f'Le produit a le prix de {float(data["data"][0]["price"])} et on peut savoir s\'il est dans la catégorie 3: True')
else:
    print(f'Le produit a le prix de {float(data["data"][0]["price"])} et on peut savoir s\'il est dans la catégorie 3 : False')







#  Si ce que je veux éventuellement obtenir serait le 'price' moyen des produits de moins de 100000 qui sont dans la catégorie 3.
#  Voyons si on peut faire cela avec le resultat de 5 produits

# # faire une demande de 25 produits (GET/products?_quantity=25)
response = requests.get(f"{BASE_URL}/products?_quantity=25&_locale=fr_CA")


 
# # json.dumps permet d'ajouter des arguments
# # indent permet de spécifier le niveau d'imbication des éléments de la réponse
resultat = json.dumps(response.json(),indent=4)


# changer un string en un dictionnaire avec json.load
# using json.loads() method
dict_resultat = json.loads(resultat)
# le data de liste_resultat est une liste de dictionnaire de produits


liste_produits = dict_resultat["data"]
total_prix = 0
cpt_produits_dans_categorie3 = 0
for produit in liste_produits:
    if (3 in produit["categories"] and prix<100000):
        total_prix += prix
        cpt_produits_dans_categorie3 += 1
moyenne = total_prix /  cpt_produits_dans_categorie3
print(f"Parmi les 25 produits que j'ai obtenu, il y a {cpt_produits_dans_categorie3} produits dans la catégorie 3 et leur prix moyen est de  {round(moyenne,2)}")

