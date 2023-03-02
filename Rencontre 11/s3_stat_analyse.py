import os
import s2_req_produit_api as s2
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

# On cherche ici à produire un fichier texte avec une courte analyse des données de ventes.
# Pour chaque valeur produite, vous devez écrire une phrase indiquant à quoi correspond cette valeur.

# Globalement :
#   Nombre total d'articles vendus
#   Montant total des ventes
#   Prix moyen des commandes

#   Personne ayant fait la commande la plus élevée avec le montant de la commande
#   Personne ayant fait la commande la moins élevée avec le montant de la commande

#Pour des points supplémentaires, vous pouvez aussi extraire les informations suivantes :
# Par catégorie :
#   Nombre total d'articles vendus
#   Montant total des ventes

info_clients = s2.addition_info()
def analyse_donnees():
    Nb_articles = 0
    Montant_ventes = 0
    Nb_clients =  30
    commande_max=  0
    commande_min = 100000
    nom_max = ""
    nom_min = ""
    prenom_max = ""
    prenom_min = ""
    for ls in range(len(info_clients)):
        commande_individuel = 0
        for dict in info_clients[ls]["commande"]:
            if not dict["quantite"] == 0:
                Nb_articles += dict["quantite"]
                Montant_ventes += (dict["prix"] * dict["quantite"])
                commande_individuel += (dict["prix"] * dict["quantite"])
        if commande_max < commande_individuel:
            commande_max = commande_individuel
            nom_max = info_clients[ls]["nom"]
            prenom_max = info_clients[ls]["prenom"]
        if commande_min > commande_individuel:
            commande_min = commande_individuel
            nom_min = info_clients[ls]["nom"]
            prenom_min = info_clients[ls]["prenom"]
            
            
    Montant_ventes = round(float(Montant_ventes),2)           
    print(80*"-")
    print(f'Le nombre d\'articles global est de {Nb_articles}')
    print(f'Le montant total des ventes est de {Montant_ventes}, $')
    Moyen_commande = round(float(Montant_ventes / Nb_clients),2)
    print(f'Le prix moyen des commandes est de {Moyen_commande} $')
    print(f'La personne ayant la commande la plus élevée est {prenom_max} {nom_max}, soit de {commande_max} $')
    print(f'La personne ayant la commande la moins élevée est {prenom_min} {nom_min}, soit de {commande_min} $')
    
analyse_donnees()

            
