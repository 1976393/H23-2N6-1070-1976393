from multiprocessing.connection import answer_challenge


class Voiture:
    def __init__(self, marque, modele, annee,  kilometrage, couleur, prix, etat = "neuf"):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = kilometrage
        self.couleur = couleur
        self.prix = prix
        self.etat = etat
        
    def imprimer_infos(self):
        print(f'{self.marque} {self.modele} {self.annee} de couleur {self.couleur}, avec seulement {self.km} km. Pour un prix raisonnable de {self.prix}$ (payable en 12 versements de {int(self.prix) / 12}$. Dans un état {self.etat}!!!')
        
voiture1 = Voiture("Toyota", "Tercel", "1972", 12888888, "rouge", 123, "Superbe")
voiture2 = Voiture("Ford", "F-150", "2015", "483759", "bleu", "2552")

voiture1.imprimer_infos()
voiture2.imprimer_infos()