from operator import index


class Personne:
    def __init__(self,nom,prenom,date_naissance) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        
class Joueur(Personne):
    def __init__(self,nom,prenom,date_naissance,no_chandail,position) -> None:
        super().__init__(nom,prenom,date_naissance)
        self.no_chandail = no_chandail
        self.position = position
        
class Attaquant(Joueur):
    def __init__(self,nom,prenom,date_naissance,no_chandail,position,nb_tirs_au_but,nb_assistance) -> None:
        super().__init__(nom,prenom,date_naissance,no_chandail,position)
        self.nb_tirs_au_but = nb_tirs_au_but
        self.nb_assistance = nb_assistance
    def compter_but(self):
        self.nb_tirs_au_but +=1

        
class Defenseur(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position,nb_interceptions,nb_passes) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_interceptions = nb_interceptions
        self.nb_passes = nb_passes
        
class Gardien(Joueur):
    def __init__(self, nom, prenom, date_naissance, no_chandail, position,nb_arrets,nb_tirs_essuyes) -> None:
        super().__init__(nom, prenom, date_naissance, no_chandail, position)
        self.nb_arrets = nb_arrets
        self.nb_tirs_essuyes = nb_tirs_essuyes
    def arreter_tir(self):
        self.nb_arrets +=1
        
guardien_Logan_Ketterer = Gardien("Logan","Ketterer","9 novembre 1993", "no 1","gardien",128,208)

defenseur_Zachary_Brault_Guillard = Defenseur("Zachary","Brault-Guillard","5 mars 1991","no 15","defenseur",32,44)

attaquant_Sunusi_Ibrahim = Attaquant("Sunusi","Ibrahim","1 octobre 2002","no 14","attaquant",23,44)

print(guardien_Logan_Ketterer.date_naissance)
print(defenseur_Zachary_Brault_Guillard.date_naissance)
print(attaquant_Sunusi_Ibrahim.date_naissance)
print(f'{guardien_Logan_Ketterer.no_chandail} et {guardien_Logan_Ketterer.position}')
print(guardien_Logan_Ketterer.nb_arrets)
guardien_Logan_Ketterer.arreter_tir()
print(guardien_Logan_Ketterer.nb_arrets)

class Equipe(Joueur):
    nb_joueur = 0
    def __init__(self, nbr_joueurs_dans_ligue,nom_equipe,liste_joueurs = []) -> None:
        self.nbr_joueurs_ligue = nbr_joueurs_dans_ligue
        self.liste_joueurs = liste_joueurs
        self.nom_equipe = nom_equipe
    def engager_joueur(self,nom_joueur):
        self.liste_joueurs.append(nom_joueur)
        Equipe.nb_joueur +=1
    def ejecter_joueur(self,nom_joueur):
        self.liste_joueurs.pop(nom_joueur)
        Equipe.nb_joueur -=1
        
cf_montreal = Equipe(3, "cf_montreal", ["Joueur1","Joueur2","Joueur3"])
print(cf_montreal.liste_joueurs)
cf_montreal.ejecter_joueur(1)
cf_montreal.engager_joueur("Bob")
print(cf_montreal.liste_joueurs)