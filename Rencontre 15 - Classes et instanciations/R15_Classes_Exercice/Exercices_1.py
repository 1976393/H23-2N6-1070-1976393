class Compte:
    def __init__(self, no_compte, type_compte, nip_client, solde = 0):
        self.no_compte = no_compte
        self.type_compte = type_compte
        self.nip_client = nip_client
        self.solde = solde
        
    def retirer(self, montant):
        if self.solde - montant < 0:
            print("Erreur, pas assez d'argent")
        else:
            self.solde - montant
    
    def ajouter(self, montant):
        self.solde += montant
        
compte1 = Compte("12345678","chèque", "888888888")
compte2 = Compte("23456789","éparge", "888888888")

compte1.retirer(100)
compte1.ajouter(1000)
compte1.ajouter(2000)
print(compte1.solde)
compte2.ajouter(5000)
print(compte2.solde)