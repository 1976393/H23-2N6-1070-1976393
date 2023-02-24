import requests
import json


base_url="https://fakestoreapi.com"


# Q1 écrivez une fonction appelée request_from qui aura 2 paramètres optionnels
#    le type d'objets que vous voulez allez chercher  et le nombre d'objets de ce type

# faites une validation pour le type d'objets car fakestoreapi.com ne vous permet d'aller chercher que des 
#       products, carts et des user

# Si le nombre d'objets désirés n'est pas entré, envoyez 1 objet du type demandé

# La fonction retournera le nombre d'objet du type désiré en autant que le type est products, carts ou user

def request_from(typ_obj, Nb_obj=1):
    if typ_obj == "products" or typ_obj == "carts" or typ_obj == "users":
        req = requests.get(f'{base_url}/{typ_obj}?limit={Nb_obj}')
        donne_req = req.json()
        donne_req_dumps = json.dumps(donne_req)
        data = json.loads(donne_req_dumps)
        return data
    else:
        print("Veuillez entrer un objet valide")


         

# Q2 ajouter une section qui permettra d'utiliser ce fichier en tant que script ou que module

# Lorsqu'il est exécuté en tant que script, ce fichier devrait faire une requête pour 1 seule produit.
# Puis il devrait imprimer un message dans le terminal indiquant si la requête à été un success ou nom.

# if __name__ == '__main__':
#     request_from(input(),1)
# else:
#     print("Aucune reuquete achemine")
        


