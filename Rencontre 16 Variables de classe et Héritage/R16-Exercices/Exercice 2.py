class Voiture:
    def __init__(self,marque,modele,annee,kilometrage,couleur,prix,etat = "neuf") -> None:
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.couleur = couleur
        self.prix = prix
        self.etat = etat
        
        def imprimer_infos(self):
            print()
        pass

class Voiture_electrique(Voiture):
    def __init__(self, marque, modele, annee, kilometrage, couleur, prix, autonomie_max, autonomie_actuelle, type_recharge, etat="neuf", ) -> None:
        super().__init__(marque, modele, annee, kilometrage, couleur, prix, etat)
        self.autonomie_max = autonomie_max
        self.autonomie_actuelle = autonomie_actuelle
        self.type_recharge = type_recharge
        
    def recharger(self, temps, recharge):
        self.autonomie_actuelle += (temps / recharge) * 40
        if (self.autonomie_actuelle > self.autonomie_max):
            self.autonomie_actuelle = self.autonomie_max
        
auto_Paul = Voiture_electrique("Audi","Q8","2021","10","Jaune","68000",400,30,"Rapide(100kw)")

auto_Lucie = Voiture_electrique("Chevrolet","Silverado","2023","10","Argent","86000",640,30,"Rapide(300kw)")

print(auto_Lucie.autonomie_actuelle)
print("Recharger auto de Lucie 10 minutes")
auto_Lucie.recharger(10,2)
print(auto_Lucie.autonomie_actuelle)
print(80*"_")
print(auto_Paul.autonomie_actuelle)
print("Recharge auto de Paul 10 minutes")
auto_Paul.recharger(10,8)
print(auto_Paul.autonomie_actuelle)