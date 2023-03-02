import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# Vous devez lire et extraire les informations du csv "data_ventes.csv"
# Le format de ce csv ne permet pas d'extraire les données très facilement.
# Regardez-le avant de commencer.

# Pour chaque client, il y la quantité de chacun des produits qu'ils ont achetés. 
# Les ids des produits sont dans l'en-tête et en ordre. 
# Donc les valeurs dans la colonne prodID1 correspondent à la quantité du produit dont l'ID est 1.
# Il en est ainsi pour chacun des 20 produits disponibles.

# Le but ultime de ce script est d'arriver à une liste, contenant pour chaque client

def csv_data_extract():
    with open("data_ventes.csv","r",encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        #Saut de 5 lignes
        for index in range(5):
            next(csv_reader)
        ls_clients_raw = []
        #Ajout des lignes du csv non modifiees à ls_clients_raw et création de la liste finale ls_clients
        for line in csv_reader:
            ls_clients_raw.append(line)
        ls_clients = []
        #Pour chaque liste de ls_clients_raw, 
        #- Creation de dictionnaires sans informations
        #- Update le dictionnaire avec les informations des listes
        #- Création d'une liste à mettre les prochaines informations nommé liste_commande
        #- Compteur mit à 1 (productId débute à 1)
        for ls in ls_clients_raw:
            dict_clients = {"userId":"","nom":"","prenom":"","commande":[{"productId":"","quantite":[{}]}]}
            dict_clients.update({"userId": ls[0],"nom":ls[1],"prenom":ls[2]})
            liste_commande = []
            cpt = 1
            
            #De 3 à la fin de la liste,
            #- Creation de dictionnaires sans informations 
            #- Update les dictionnaires avec le compteur et l'info des listes
            #- Ajout du dictionnaire à la fin de la liste
            #- Augmentation du compteur
            for info in ls[3:]:
                dict = {"productId":"","quantite":""}
                dict.update({"productId":cpt,"quantite":int(info)})
                liste_commande.append(dict)
                cpt+=1
            #Ajout des informations de commande au dictionnaire de client
            #Ajout du dictionnaire client à la liste d'informations des client; ls_clients
            dict_clients.update({"commande":liste_commande})
            ls_clients.append(dict_clients) 
        #print(ls_clients)
        return (ls_clients)
        
        
# csv_data_extract()
