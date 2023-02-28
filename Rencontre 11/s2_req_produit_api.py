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

info = []
info = s1.csv_data_extract()



def addition_info():
    data_api_req = requests.get(f'{url}products?limit=20')
    data_api_json = data_api_req.json()
    data_api_dumps = json.dumps(data_api_json,indent=4)
    data_api = json.loads(data_api_dumps)
    # print(data_api)
    
    for ls in range(len(info)):
        for dict in info[ls]["commande"]:
            for ls_api in data_api:
                if dict["productId"] == ls_api["id"]:
                    price = {"prix":""}
                    categorie = {"categorie":""}
                    price.update({"prix": ls_api["price"]})
                    categorie.update({"categorie":ls_api["category"]})
                    info[ls]["commande"][dict["productId"]-1].update(price)
                    info[ls]["commande"][dict["productId"]-1].update(categorie)
    indented_data = json.dumps(info,indent=4)
    print(indented_data)
            
            
            
            
            # for id in range(len(dict)):
                
            # for id in ls["commande"][index]:
            #     print(id)
                #print(ls["commande"][index]["productId"])
            # for id in ls_commande:
                

addition_info()
