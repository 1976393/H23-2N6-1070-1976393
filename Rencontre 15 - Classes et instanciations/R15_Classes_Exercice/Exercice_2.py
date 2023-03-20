from datetime import datetime
import random


class Inscription:
    def __init__(self, alias, role, no_confirmation = 0, date_inscription = datetime.date, cout = 45):
        self.date_inscription = date_inscription
        self.alias = alias
        self.role = role
        self.cout = cout
        self.no_confirmation = no_confirmation
        
    def confirmer(self):
        no_confirmation = random.randint(1,100000)
        self.no_confirmation += no_confirmation
        print(f'Félicitation {self.alias}! Vous êtes inscrit dans le rôle de {self.role}. Voici votre numéro de confirmation: {self.no_confirmation} ')
        
    def canceller(self):
        no_confirmation = random.randint(1,100000)
        self.no_confirmation += no_confirmation
        print(f'Votre inscription au numéro de confirmation: {self.no_confirmation} a été cancellée')
        self.no_confirmation = 0
        
inscription1 = Inscription("Gandalf le magnifique", "Magicien")
inscription1.confirmer()
inscription2 = Inscription("Thornal le ténébrreux", "Guerrier")
inscription2.confirmer()
inscription2.canceller()
print(inscription2.no_confirmation)