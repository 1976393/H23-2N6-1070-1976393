from abc import ABC,abstractmethod

class OBNL():
    def __init__(self) -> None:
        liste_donateurs = []
        self.liste_donateurs = liste_donateurs
        
    def afficher_dons(self):
        for i in self.liste_donateurs:
            print(f'Don de: {i.nom} \n - montant net de: {i.donner()}')

class Donateur(ABC):
    def __init__(self,nom,estPublique) -> None:
        self.nom = nom
        self.estPublique = estPublique
    
    @abstractmethod    
    def donner():
        pass
    
class Donateur_Riche(Donateur):
    def __init__(self, nom, estPublique,contribution) -> None:
        super().__init__(nom, estPublique)
        self.contribution = contribution
        
    def donner(self):
        return self.contribution
    
class Donateur_Expert(Donateur):
    def __init__(self, nom, estPublique,contribution,expertise) -> None:
        super().__init__(nom, estPublique)
        self.contribution = contribution
        self.expertise = expertise
        
    def donner(self):
        return (self.contribution * 120)
    
don1 = Donateur_Riche("Marc Tremblay","non publique",120000)
don2 = Donateur_Riche("Jean Tremblay","publique",1200000)
don3 = Donateur_Expert("Pierre Johnson","publique",120,"comptabilité")

obnl = OBNL()
obnl.liste_donateurs.append(don1)
obnl.liste_donateurs.append(don2)
obnl.liste_donateurs.append(don3)

obnl.afficher_dons()
