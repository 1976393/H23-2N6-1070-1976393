#from curses.ascii import isdigit
import requests
import json


base_url="https://fakestoreapi.com"

# Q1 Écrivez une fonction appelée request_carts qui aura 1 paramètre
#   soit le nombre de carts que vous voulez aller chercher
#   Le nombre de cart doit être donné lors de l'appel de la fonction 
#           mais s'il n'est pas donné il faut que cela ne cause pas d'erreur
#   Si le nombre de cart n'est pas donné lors de l'appel, 
#           donnez un message comme quoi il faut préciser le nombre de carts 
#           et arrêter l'exécution de la fonction
#   Vérifiez que le nombre donné lors de l'appel est entre 1 et 10
#   Si ce n'est pas le cas, 
#          donnez un message comme quoi il faut demander entre 1 et 10 carts, 
#          en précisant le nombre de carts qui avait été demandé
#   Si on passe autre chose qu'un nombre entier en paramètre 
#          faites un message comme quoi il faut entrer un nombre entre 1 et 10

#   La fonction doit retourner les carts obtenu avec la requête get du site webs. Mais seulement si le nombre de carts demandés est entre 1 et 10
def requests_carts(Nb_carts):
    if Nb_carts == "None":
        print("Veuillez entrer un nombre de cart")
    else:
        if type(Nb_carts)==str:
            print(f'Veuillez entrer un nombre de carts entre 1 et 10, votre demande : {Nb_carts}')
        elif not Nb_carts <11 or not Nb_carts >0:
            print(f'Veuillez entrer un nombre de carts entre 1 et 10, votre demande : {Nb_carts}')
        else:
            req = requests.get(f'{base_url}/products?limit={Nb_carts}')
            donne_req = req.json()
            donne_req_dump = json.dumps(donne_req,indent=4)
            print(donne_req_dump)





# Q2 Écrivez une fonction appelée request_products qui aura 1 paramètre
#   soit le nombre de produits que vous voulez aller chercher
#   Le nombre de produit doit soit être donné lors de l'appel de la fonction
#                             soit être demandé à l'usager s'il n'est pas donné
#   Vérifiez que le nombre demandé est entre 1 et 10
#   Limitez cette valeur à 10 si l'usager en demande plus et donnez un message comme quoi vous avez cette limite
#   Si le nombre demandé est moins de 1, obtenez 1 produit tout simplement

#   La fonction doit retourner le nombre de produits demandés, si le nombre est entre 1 et 10

def request_products(Nb_produits):
     if Nb_produits == "None":
        print("Veuillez entrer un nombre de cart")
     else:
        if type(Nb_produits)==str:
            print(f'Veuillez entrer un nombre entre 1 et 10, votre demande : {Nb_produits}')
        elif not Nb_produits <11 or not Nb_produits >=1:
            print(f'Veuillez entrer un nombre entre 1 et 10, votre demande : {Nb_produits}')
        elif Nb_produits >10:
            print("La limite pour la demande est de 10, Veuillez entrer un nombre entre 1 et 10")
        elif Nb_produits < 0:
            Nb_produits = 1
            req = requests.get(f'{base_url}/products?limit={Nb_produits}')
            donne_req = req.json()
            donne_req_dump = json.dumps(donne_req,indent=4)
            print(donne_req_dump)
        else:
            req = requests.get(f'{base_url}/products?limit={Nb_produits}')
            donne_req = req.json()
            donne_req_dump = json.dumps(donne_req,indent=4)
            print(donne_req_dump)

requests_carts(1)





