import os
import requests
import json

os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Maintenant que nous avons un script capable de lire et décoder le fichier csv.
# Nous voulons ajouter des informations à liste de produits de chaque client
#       le prix de chaque produit et sa catégorie

# Les informations sur les produits proviennent du site du magasin.
# Vous devez aller chercher les informations à l'aide du module requests.
url = "https://fakestoreapi.com/"

import s1_lire_csv_ventes as s1

#Résultat du script 1 mis dans info
info = []
info = s1.csv_data_extract()



def addition_info():
    #Requêtes des informations du API mises dans data_api
    data_api_req = requests.get(f'{url}products?limit=20')
    data_api_json = data_api_req.json()
    data_api_dumps = json.dumps(data_api_json,indent=4)
    data_api = json.loads(data_api_dumps)
    # print(data_api)
    
    #Passement au travers de chaque ligne de info
    for ls in range(len(info)):
        #Passement au travers de chaque dictionnaire de ["commande"]
        for dict in info[ls]["commande"]:
            #Passement au travers de chaque ligne du data de l'api
            for ls_api in data_api:
                
                #Si le productId de info est le même que le id des informations de l'api
                #- création de dictionnaires sans informations
                #- update des dictionnaires avec le prix et la categorie de l'id qui est le même
                #- update du dictionnaire commande dans la variable info à la position du id 
                # dans la liste de dictionnaire commande -1 (position du id dans la liste est 1 de moins que le id)
                
                if dict["productId"] == ls_api["id"]:
                    price = {"prix":""}
                    categorie = {"categorie":""}
                    price.update({"prix": ls_api["price"]})
                    categorie.update({"categorie":ls_api["category"]})
                    info[ls]["commande"][dict["productId"]-1].update(price)
                    info[ls]["commande"][dict["productId"]-1].update(categorie)
    # indented_data = json.dumps(info,indent=4)
    # print(indented_data)
    # print(info)
    return(info)
#addition_info()
